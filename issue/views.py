from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Room, Incharge, Token, Display_call
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.
def display(request):
    context = {}
    a = Display_call.objects.get(d_room_no=1)
    b = Display_call.objects.get(d_room_no=2)
    c = Display_call.objects.get(d_room_no=3)
    d = Display_call.objects.get(d_room_no=4)
    e = Display_call.objects.get(d_room_no=5)
    f = Display_call.objects.get(d_room_no=6)
    g = Display_call.objects.get(d_room_no=7)
    h = Display_call.objects.get(d_room_no=8)
    i = Display_call.objects.get(d_room_no=9)
    j = Display_call.objects.get(d_room_no=10)

    context["room_1"] =a.d_tok_no
    context["room_2"] =b.d_tok_no
    context["room_3"] =c.d_tok_no
    context["room_4"] =d.d_tok_no
    context["room_5"] =e.d_tok_no
    context["room_6"] =f.d_tok_no
    context["room_7"] =g.d_tok_no
    context["room_8"] =h.d_tok_no
    context["room_9"] =i.d_tok_no
    context["room_10"] =j.d_tok_no
    return render(request, 'mydisplay.html', context)

@login_required(login_url = 'login')
def panel(request):
    z = request.user
    print(z)
    y = z.room
    y = str(y)
    print(y)
    if (y == 'Counter_1'):
        r_x = 1;
    elif(y == 'Counter_2'):
        r_x = 2;
    elif(y == 'Counter_3'):
        r_x = 3;
    elif(y == 'Counter_4'):
        r_x = 4;
    elif(y == 'Counter_5'):
        r_x = 5;
    elif(y == 'Counter_6'):
        r_x = 6;
    elif(y == 'Counter_7'):
        r_x = 7;
    elif(y == 'Counter_8'):
        r_x = 8;
    elif(y == 'Counter_9'):
        r_x = 9;
    elif(y == 'Counter_10'):
        r_x = 10;
    else:
        r_x = 1000;             # Any Value

    context = {}
    fresh_call = '-';
    x = ''
    pr = ''
    var = '-'
    issue_time = ''
    if (request.method == 'POST'):
        a = request.POST
        # var = request.POST['test']
        # if(var == 'served'):
        if 'served' in request.POST:
            try:
                # tok_serve = Token.objects.get(room.id = 1, is_called = True, is_served = False)
                tok_serve = Token.objects.get(room__room_no = r_x, is_called = True, is_served = False)
                tok_serve.is_served = True
                tok_serve.served_time = datetime.datetime.now()
                tok_serve.save()

            except Token.DoesNotExist:
                pass

        # print(var)
        # if (var == "call_token"):                 #Token is called here
        if 'next' in request.POST:
            # try:
            if (Token.objects.filter(room__room_no = r_x, is_served = False).order_by("created_date").exists()):
                tok_call = Token.objects.filter(room__room_no = r_x, is_served = False).order_by("created_date")
                t_call = tok_call[0]
                t_call.is_called = True
                t_call.save()
                fresh_call = t_call.tok_no
                if (tok_call[0].is_priority):
                    pr = "PA-"
                else:
                    pr = "RA-"
                fresh_call = str(fresh_call)
                fresh_call = pr+fresh_call
                a = Display_call.objects.get(d_room_no=r_x)
                a.d_tok_no = fresh_call
                a.save()

            # except Token.DoesNotExist:
            else:
                fresh_call = 'No One is Called.'
    try:
        tok_called = Token.objects.get(room__room_no = r_x, is_called = True,  is_served = False)
        tok_no = tok_called.tok_no
        issue_time = tok_called.created_date
        if (tok_called.is_priority):
            suf = "PA-"
        else:
            suf = "RA-"
        suf = suf+str(tok_no)
        tok_called = suf
    except Token.DoesNotExist:
        tok_called = '-'

    tok_que = Token.objects.filter(room__room_no = r_x, is_served = False).order_by("created_date")
    tok_count = tok_que.count()
    context["r_x"] = r_x
    context["tok_que"] = tok_que
    context["tok_count"] = tok_count
    context["tok_called"] = tok_called
    context["fresh_call"] = fresh_call
    context["issue_time"] = issue_time
    return render(request, 'room_1.html', context)

@csrf_exempt
def issue(request):
    context = {}
    print('7584')
    if (request.method == 'POST'):
        a = request.POST
        p_no = 50
        tok_no = "5000"
        data = {}
        for key, val in a.items():
            if key == 'p_no':
                p_no = val
                data['p_no'] = val
            if key == 'room_no':
                room_no = val
                data['room_no'] = val
            if key == 'tok_no':
                tok_no = val
                data['tok_no'] = val

        room = Room.objects.get(room_no=1)
        if (room_no == 'A-'):
            room = Room.objects.get(room_no=1)
        if (room_no == 'B-'):
            room = Room.objects.get(room_no=2)
        if (room_no == 'C-'):
            room = Room.objects.get(room_no=3)
        if (room_no == 'D-'):
            room = Room.objects.get(room_no=4)
        if (room_no == 'E-'):
            room = Room.objects.get(room_no=5)
        if (room_no == 'F-'):
            room = Room.objects.get(room_no=6)
        if (room_no == 'G-'):
            room = Room.objects.get(room_no=7)
        if (room_no == 'H-'):
            room = Room.objects.get(room_no=8)
        if (room_no == 'I-'):
            room = Room.objects.get(room_no=9)
        if (room_no == 'J-'):
            room = Room.objects.get(room_no=10)

        print(a)
        print(p_no)
        print(room_no)
        print(tok_no)
        print(data)

        token = Token.objects.create(
            is_priority=p_no,
            room=room,
            tok_no=tok_no,
        )
        token.save()
        context["form"] = 424325
    return render(request, 'issue.html', context)
