from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
	fullname = forms.CharField(widget = forms.TextInput(
					attrs={
					"class": "form-control", 
					"placeholder": "Your Name"
					}))
	email	 = forms.EmailField(widget=forms.EmailInput(attrs= {
				"class": "form-control",
				"placeholder": "your email"
		}))
	content	 = forms.CharField(widget= forms.Textarea(attrs = {
				"class": "form-control",
				"placeholder": "Your Content"

		}))	



	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("email has to be gmail.com")
		return email	

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)	

class RegisterForm(forms.Form):
	first_name = forms.CharField()
	last_name  =  forms.CharField()
	username   =  forms.CharField()
	password   =  forms.CharField(widget= forms.PasswordInput)
	password2  =  forms.CharField(label='Confirm Password', widget= forms.PasswordInput)
	email      = forms.EmailField(widget= forms.EmailInput(attrs={
							"class": "form-control",
							"placeholder": "Your email"
					}))


	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs =User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username is taken")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs =User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is taken")
		return email
		


	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("Passwords don't match")
		else:
			return data	