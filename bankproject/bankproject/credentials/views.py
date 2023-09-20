from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from .models import Register,Login
from django.http import HttpResponse
from django.template  import loader


def demo(request):
    return render(request, "index1.html")

def newForm(request):
    return render(request, "newForm.html")

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         cpass = request.POST['cpass']
#         user = User.objects.create_user(username=username, password=password)

#         user.save()
#         return redirect('login')


#     return render(request, "register.html")

# views.py
from django.shortcuts import render, redirect

def details(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phno = request.POST['phno']
        mailid = request.POST['mailid']
        address = request.POST['address']
        district = request.POST['district']
        account_type = request.POST['account-type']
        materials = ','.join(request.POST.getlist('materials'))

        # Create a BankAccount object and save it
        bank_account = Register(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phno=phno,
            mailid=mailid,
            address=address,
            district=district,
            account_type=account_type,
            materials=materials
        )
        bank_account.save()
        context = {}
        template = loader.get_template("index1.html")
        # return HttpResponse(template.render(context, request))
        return HttpResponse("<script>alert('Application Accepted');window.location='demo';</script>")

    
    else:
        print("else part")
        context = {}
        template = loader.get_template("details.html")
        return HttpResponse(template.render(context, request))



def form(request):
    return render(request, "form.html")


def login(request):
    if request.method == "POST":
        print("kkkk")
        uname = request.POST.get('uname')
        pwd = request.POST.get('psw')
        
        matching_users = Login.objects.filter(uname=uname, pwd=pwd)
        print("kkkkl",matching_users)
        if matching_users.exists():
            return HttpResponse("<script>alert('User Registration Successfully');window.location='newForm';</script>")


        else:
            messages.error(request, 'Invalid username or password')
            return HttpResponse("<script>alert('invalid uname or pwd');window.location='/login';</script>")

    else:
        return render(request, 'login.html')


def register(request):
    print("hiiii")
    if request.method == 'POST':
        print("post")
        uname= request.POST['username']
        pwd = request.POST['password']
        cpwd = request.POST['confirm-password']
    
        regi = Login(uname=uname,pwd=pwd,cpwd = cpwd)
        regi.save()
        context = {}
        template = loader.get_template("login.html")
        # return HttpResponse(template.render(context, request))
        return HttpResponse("<script>alert('User Registration Successfully');window.location='login';</script>")
    
    else:
        print("else part")
        context = {}
        template = loader.get_template("Register.html")
        return HttpResponse(template.render(context, request))
    


            