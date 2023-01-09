from django.shortcuts import render, redirect
from .forms import RegistrationForm, AssignUserForm
from .models import Account, UserProfile
from issue.models import Token
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.utils.timezone import datetime
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print('1')
        if form.is_valid():
            print('2')
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name,  email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            # messages.success(request, 'Registration successful')
            # return redirect('register')

            # # Create a user profile
            # profile = UserProfile()
            # profile.user_id = user.id
            # profile.profile_picture = 'default/default-user.png'
            # profile.save()

            # User Activation
            current_site = get_current_site(request)
            mail_subject = "Please activate your Account"
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, "Thank you for registering with us. We have sent you a verification Email. Please verify")
            return redirect('/accounts/login/?command=verification&email=' + email)
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'You are now logged in')
            return redirect('panel')
        else:
            messages.error(request, 'Invalid Login Credentials')
            return redirect('login')
    # return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('login')



def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            # with ! it ignores Snall case or big case
            user = Account.objects.get(email__exact=email)

            # Forgot Password Send Email
            current_site = get_current_site(request)
            mail_subject = "Reset your Password"
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Password reset Email ghas been sent.')
            return redirect('login')

        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request,'accounts/forgotPassword.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user: None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations your Account is activated')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
    return redirect('register')

@login_required(login_url='login')
def report_assign(request):

    user = Account.objects.all()
    context = {
        'user': user,
    }
    print(user)
    return render(request, 'accounts/report_assign.html', context)

@login_required(login_url='login')
def edit_assign(request):
    user = Account.objects.all()
    form = AssignUserForm()
    context = {
        'user': user,
        'form': form,
    }
    print(user)
    if request.method == 'POST':
        form = AssignUserForm(request.POST)
        if form.is_valid():
            data = form.save(commit = False)
            user = Account.objects.get(email__exact=data.user)
            user.room = data.room
            user.save()
            context["status"] = "Added successfully"
        return render(request, 'accounts/report_assign.html',  context)
    return render(request, 'accounts/edit_assign.html',  context)

@login_required(login_url='login')
def dashboard(request):
    z = request.user
    print(z)
    print(z.is_admin)
    if(z.is_admin):
        context = {}
        user = Account.objects.all().order_by("room")
        today = datetime.today()

        # r_1w = Token.objects.filter(room__room_no = 1, is_served = False, created_date__year=today.year-1, created_date__month=today.month, created_date__day=today.day).order_by("created_date")
        r1_w = Token.objects.filter(room__room_no = 1, is_served = False).order_by("created_date")
        r1_wait = r1_w.count()
        r1_s = Token.objects.filter(room__room_no = 1, is_served = True).order_by("created_date")
        r1_served = r1_s.count()
        r1_m = Token.objects.filter(room__room_no = 1, is_missed = True).order_by("created_date")
        r1_missed = r1_m.count()

        r2_w = Token.objects.filter(room__room_no = 2, is_served = False).order_by("created_date")
        r2_wait = r2_w.count()
        r2_s = Token.objects.filter(room__room_no = 2, is_served = True).order_by("created_date")
        r2_served = r2_s.count()
        r2_m = Token.objects.filter(room__room_no = 2, is_missed = True).order_by("created_date")
        r2_missed = r2_m.count()

        r3_w = Token.objects.filter(room__room_no = 3, is_served = False).order_by("created_date")
        r3_wait = r3_w.count()
        r3_s = Token.objects.filter(room__room_no = 3, is_served = True).order_by("created_date")
        r3_served = r3_s.count()
        r3_m = Token.objects.filter(room__room_no = 3, is_missed = True).order_by("created_date")
        r3_missed = r3_m.count()

        r4_w = Token.objects.filter(room__room_no = 4, is_served = False).order_by("created_date")
        r4_wait = r4_w.count()
        r4_s = Token.objects.filter(room__room_no = 4, is_served = True).order_by("created_date")
        r4_served = r4_s.count()
        r4_m = Token.objects.filter(room__room_no = 4, is_missed = True).order_by("created_date")
        r4_missed = r4_m.count()

        r5_w = Token.objects.filter(room__room_no = 5, is_served = False).order_by("created_date")
        r5_wait = r5_w.count()
        r5_s = Token.objects.filter(room__room_no = 5, is_served = True).order_by("created_date")
        r5_served = r5_s.count()
        r5_m = Token.objects.filter(room__room_no = 5, is_missed = True).order_by("created_date")
        r5_missed = r5_m.count()

        r6_w = Token.objects.filter(room__room_no = 6, is_served = False).order_by("created_date")
        r6_wait = r6_w.count()
        r6_s = Token.objects.filter(room__room_no = 6, is_served = True).order_by("created_date")
        r6_served = r6_s.count()
        r6_m = Token.objects.filter(room__room_no = 6, is_missed = True).order_by("created_date")
        r6_missed = r6_m.count()

        r7_w = Token.objects.filter(room__room_no = 7, is_served = False).order_by("created_date")
        r7_wait = r7_w.count()
        r7_s = Token.objects.filter(room__room_no = 7, is_served = True).order_by("created_date")
        r7_served = r7_s.count()
        r7_m = Token.objects.filter(room__room_no = 7, is_missed = True).order_by("created_date")
        r7_missed = r7_m.count()

        r8_w = Token.objects.filter(room__room_no = 8, is_served = False).order_by("created_date")
        r8_wait = r8_w.count()
        r8_s = Token.objects.filter(room__room_no = 8, is_served = True).order_by("created_date")
        r8_served = r8_s.count()
        r8_m = Token.objects.filter(room__room_no = 8, is_missed = True).order_by("created_date")
        r8_missed = r8_m.count()

        r9_w = Token.objects.filter(room__room_no = 9, is_served = False).order_by("created_date")
        r9_wait = r9_w.count()
        r9_s = Token.objects.filter(room__room_no = 9, is_served = True).order_by("created_date")
        r9_served = r9_s.count()
        r9_m = Token.objects.filter(room__room_no = 9, is_missed = True).order_by("created_date")
        r9_missed = r9_m.count()

        r10_w = Token.objects.filter(room__room_no = 10, is_served = False).order_by("created_date")
        r10_wait = r10_w.count()
        r10_s = Token.objects.filter(room__room_no = 10, is_served = True).order_by("created_date")
        r10_served = r10_s.count()
        r10_m = Token.objects.filter(room__room_no = 10, is_missed = True).order_by("created_date")
        r10_missed = r10_m.count()

        print('qwer')
        print(r1_wait)
        print(r1_served)
        print(r1_missed)

        context["user"] = user
        context["r1_wait"] = r1_wait
        context["r1_served"] = r1_served
        context["r1_missed"] = r1_missed

        context["r2_wait"] = r2_wait
        context["r2_served"] = r2_served
        context["r2_missed"] = r2_missed

        context["r3_wait"] = r3_wait
        context["r3_served"] = r3_served
        context["r3_missed"] = r3_missed

        context["r4_wait"] = r4_wait
        context["r4_served"] = r4_served
        context["r4_missed"] = r4_missed

        context["r5_wait"] = r5_wait
        context["r5_served"] = r5_served
        context["r5_missed"] = r5_missed

        context["r6_wait"] = r6_wait
        context["r6_served"] = r6_served
        context["r6_missed"] = r6_missed

        context["r7_wait"] = r7_wait
        context["r7_served"] = r7_served
        context["r7_missed"] = r7_missed

        context["r8_wait"] = r8_wait
        context["r8_served"] = r8_served
        context["r8_missed"] = r8_missed

        context["r9_wait"] = r9_wait
        context["r9_served"] = r9_served
        context["r9_missed"] = r9_missed

        context["r10_wait"] = r10_wait
        context["r10_served"] = r10_served
        context["r10_missed"] = r10_missed


        # orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
        # orders_count = orders.count()
        return render(request, 'accounts/dashboard.html', context)
    else:
        messages.error(request, 'Invalid Login Credentials')
        return redirect('login')



def resetPassword_validate (request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user: None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please Reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been Expired')
        return redirect('login')

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password set successfully')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html')
