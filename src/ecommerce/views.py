from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm
from .forms import LoginForm
from .forms import RegisterForm


def home_page(request):
	context = {

		"title": "New Home Page",
		"content": "this is the home page",
	}
	if request.user.is_authenticated():
		context["premium_content"] = "Yaassss!"

	return render(request, "home_page.html", context)

def about_page(request):
	context = {

		"title": "about page",
		"content": "this is the about page"

	}
	return render(request, "about_page.html", context)


def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title": "contact_page",
		"content": "Welcome to the contact page",
		"form" : contact_form
	}

	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method =="POST":
	# 	# print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request, "contact/views.html", context)


def login_page(request):
	form = LoginForm(request.POST or None) 
	context = {
		"form": form
		}	
	print("user logged in")
	print(request.user.is_authenticated())

	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")

		user = authenticate(request, username=username, password=password)
		print(request.user.is_authenticated())
		
		if user is not None:
			print(request.user.is_authenticated())
			login(request,user)
	    # Redirect to a success page.
			# context['form'] = LoginForm()
			return redirect("/login")
    
		else:
    # Return an 'invalid login' error message.
   			print("Error")

	return render(request, "auth/login.html", context) 

User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {

		"form": form
	}
	if form.is_valid():
		print(form.cleaned_data)

		firstname = form.cleaned_data.get("firstname")
		lastname = form.cleaned_data.get("lastname")
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		email = form.cleaned_data.get("email")
		new_user = User.objects.create_user(username,password, email)
		print(new_user)

	return render(request, "auth/register.html",context)


def application_page(request):

	context = {

		"title": "application_page",
		"content": "this is the application page"
	}
	return render(request, "application_page.html", context)			


def home_page_old(request):
	html_ = """
	<!doctype html>
	<html lang="en">
		<head>
		    <!-- Required meta tags -->
		    <meta charset="utf-8">
		    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

		    <!-- Bootstrap CSS -->
		    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


		    <title>Hello, world!</title>


		</head>
		<body>

		<div class = 'text-center'>
		    <h1>Hello, world!</h1>
		</div>    
		    <!-- Optional JavaScript -->
		    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
		    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
		    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
		    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
		</body>
	</html>
	"""
	return HttpResponse(html_)