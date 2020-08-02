from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def home(request):
	return render(request,'real_home.html')

def register(request):
	if request.method=='POST':
		username=request.POST['username']
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']
		if password2!=password1:
			messages.info(request,'password are not matching')
			return redirect('register')
		elif User.objects.filter(username=username).exists():
			messages.info(request,'username already exists')
			return redirect('register')
		else:
			user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
			user.save()
			return redirect('login')
	return render(request,'home.html')

def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			messages.info(request,'not an authenticate user')
			return redirect('login')
	return render(request,'login.html')


def logout(request):
	auth.logout(request)
	return redirect('home')