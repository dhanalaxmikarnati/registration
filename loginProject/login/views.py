from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
          auth.login(request,user)
          return redirect("/")
        else:
           messages.info(request,"invalid credentials")
           return redirect('login')
    else:
      return render(request,'login.html')
   
   
def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if(password1==password2):
             if User.objects.filter(username=username).exists():
                User.info(request,'Username already taken')
                return redirect('register')
             elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
             else :
                   user = User.objects.create_user(username=username,firstname=firstname,lastname=lastname,email=email,password=password1)
                   user.save();
                   print('user created')
                   return redirect('login/')
        else:
            
             print("password not matching....")
             return redirect('register')
    else:
        return render(request,'register.html')  

def logout(request):
   auth.logout(request)
   return redirect('/')