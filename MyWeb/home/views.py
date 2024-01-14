from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.template import loader

from django.shortcuts import render
from .models import Member
from .forms import MemberForm
def home(request):
    return render(request, "home/home.html", {})






         



def Regestration(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if request.POST.get('passwd')==request.POST.get('confirm_passwd'):
            if form.is_valid():
                form.save()
                return render(request, 'home/login.html', {})
            else:
                return render(request, 'home/regest.html', {'error_message':'password and confirm password are not the same'})


            

        else:
            return render(request, 'home/regest.html')

        


    else:
        return render(request, 'home/regest.html', {})
        
            


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username exists
        user = Member.objects.filter(User_name=username).first()

        if user is not None:
            # User exists, check password
            if password == user.passwd:
                

                return render(request, 'home/mypage.html', {'username':user})
            else:

                return render(request, 'home/login.html', {'error_message':'incorect password'})
        else:
            return render(request, 'home/login.html', {'error_message':'incorect user'})

    else:
        return render(request, 'home/login.html', {})



