from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request):
    if (request.method == 'POST'):
        print('home')
    return render(request, 'home2.html')
    # return HttpResponse('New Home Page....')
