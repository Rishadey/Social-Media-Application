from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import *
import os
# Create your views here.
def testing(request):
    return HttpResponse('testing the page')

def dele(request,id):
    d=user.objects.get(id=id)
    d.delete()
    return redirect("../adminlogin")

#REGISTRATION
def registration(request):
    return render(request,'registration.html')
from .models import user 
def registercode(request): 
     u = user() # This is your custom user model 
     u.fullname = request.GET['fullname'] 
     u.username = request.GET['username'] 
     u.phno = request.GET['phno'] 
     u.email = request.GET['email'] 
     u.pwd = request.GET['pwd'] 
     u.conpwd = request.GET['conpwd'] 
     u.gender = request.GET['gender'] 
     if u.username and u.pwd and u.email and u.phno: 
        user_instance = user( fullname=u.fullname, 
                             username=u.username, 
                             email=u.email, 
                             phno=u.phno, 
                             pwd=u.pwd, 
                             conpwd=u.conpwd, 
                             gender=u.gender )
        user_instance.save() # Assuming you have a login function for your custom model # You might need to create one if not using Django's built-in auth 
        return redirect('../login') 
     u.save() 
     return render(request, 'registration.html')


def button(request):
        return redirect('../main')

def buttonlogin(request):
        return redirect('../login')

def barbutton(request):
        return redirect('../login')

def buttonhome(request):
        return redirect('../index')

#LOGIN
def login(request):
     return render(request, 'login.html')
def logincode(request):
    u=user()
    a=request.GET['a1']
    b=request.GET['a2']
    if user.objects.filter(email=a,pwd=b):
        if a and b:
            u.email = a
            u.pwd = b
        return render(request,'index.html')
    else:
        return render(request,'login.html')

#APP
def index(request):
    a=picfile.objects.all()
    return render(request,'index.html',{'x':a})

def main(request):
    a=picfile.objects.all()
    return render(request,'main.html',{'x':a})

def post(request):
     a=picfile.objects.all()
     return render(request,'post.html')


def handel_upd(file,filename):
    if not os.path.exists('app/static/upload/'):
        os.mkdir('app/static/upload')
    with open('app/static/upload/'+filename,'wb+') as dest:
        for c in file.chunks():
            dest.write(c)

def upload(request):
    return render(request,'upload.html')
def upd(request):
    if request.method=='POST':
        handel_upd(request.FILES['a2'],str(request.FILES['a2']))
        url="upload/"+str(request.FILES['a2'])
        u=picfile()
        u.pname=request.POST['a1']
        u.purl=url
        u.save()
        return redirect("../index")


