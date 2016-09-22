from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (
	login as auth_login,
	logout as auth_logout
)
from profiles.form import RegistrationForm, LoginForm

def register(request):
	form = RegistrationForm()

	if request.method == 'POST':
		form = RegistrationForm(request.POST)

		if form.is_valid():
			form.save()

			messages.info(
				request,
				'Kayıt başarılı. Şimdi login olabilirsiniz.'
			)

			return redirect('login')

	return render(request, 'register.html', {

		'title': 'Kayıt Ol',
		'form': form,

	})

def login(request):
	form = LoginForm()

	if request.method == 'POST':
		form = LoginForm(request.POST)
		request.session['name'] = request.POST['username']
		if form.is_valid():
			auth_login(request, form.user)
			# messages.info(
			# 	request,
			# 	'Giriş yaptınız.'
			# )

			return redirect('/')

	return render(request, 'login.html', {

		'title': 'Giriş Yap',
		'form': form,

	})


def logout(request):
	auth_logout(request)
	return redirect('/')


