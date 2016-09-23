from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import Customer, Employee, Services, Sales_Slip, Sales_Slip_Action,User
from mbella.form import (
    CustomerCreationForm, EmployeeCreationForm, ServicesCreationForm, SalesSlipCreationForm, SaleSlipActionCreationForm, LoginForm, RegistrationForm
)
from django.contrib.auth.decorators import login_required


from django.contrib.auth import (
	login as auth_login,
	logout as auth_logout,
    authenticate
)






# def logout(request):
# 	auth_logout(request)
# 	return redirect('/')





# Create your views here.

def home(request):
    if request.session.get('user_id'):
        salesslips = Sales_Slip.objects.all().filter(user_id=request.session.get("user_id"))
        return render(request, 'home.html',
            {
                'title' : 'AnaSayfa',
                'salesslips' : salesslips,
            }
        )
    else:
        return redirect("login")

# def home(request):
#     customers = Customer.objects.all()
#     return render(request, 'home.html',
#         {
#             'title': 'AnaSayfa',
#             'customers' : customers,
#         }
#     )
@login_required(login_url='login')
def musteriler(request):
    customers = Customer.objects.all()
    form = CustomerCreationForm()

    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.info(
                request,
                'Kayıt başarılı.'
            )

            return redirect('/musteriler')

    return render(request, 'musteriler.html',
        {
            'title' : 'Müşteriler',
            'form' : form,
            'customers' : customers,
        }
    )

@login_required(login_url='login')
def calisanlar(request):
    employees = Employee.objects.all()
    form = EmployeeCreationForm()

    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.info(
                request,
                'Kayıt başarılı.'
            )
            return redirect('/calisanlar')

    return render(request, 'calisanlar.html',
        {
            'title': 'Çalışanlar',
            'form' : form,
            'employees': employees,
        }
    )

@login_required(login_url='login')
def hizmetler(request):
    servicess = Services.objects.all()
    form = ServicesCreationForm()

    if request.method == 'POST':
        form = ServicesCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.info(
                request,
                'Kayıt başarılı.'
            )
            return redirect('/hizmetler')

    return render(request, 'hizmetler.html',
        {
            'title' : 'Hizmetler',
            'servicess' : servicess,
            'form': form
        }
    )
@login_required(login_url='login')
def raporlar(request):
    salesslips = Sales_Slip.objects.all()
    form = SalesSlipCreationForm()

    if request.method == 'POST':
        form = SalesSlipCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.info(
                request,
                'Kayıt başarılı.'
            )
            return redirect('/raporlar')

    return render(request, 'raporlar.html',
        {
            'title' : 'Raporlar',
            'form' : form,
            'salesslips' : salesslips,
        }
    )


def yeni_musteri(request):
    form = CustomerCreationForm()

    if request.method == 'POST':
        form = CustomerCreationForm (request.POST)

        if form.is_valid():
            form.save()
            messages.info(
                request,
                'Kayıt başarılı.'
            )
            return redirect('/musteriler')

    return render(request, 'yeni_musteri.html',
                  {
                      'title' : 'Yeni Müşteri',
                      'form' : form,
                  }
            )


def yeni_hizmet(request):
    form = ServicesCreationForm()

    if request.method == 'POST':
        form = ServicesCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(
                request,
                'Kayıt başarılı.'
            )
            return redirect('/hizmetler')

    return render(request, 'yeni_hizmet.html',
                  {
                      'title' : 'Yeni Hizmet',
                      'form' : form
                  }
            )

def yeni_calisan(request):
    form = EmployeeCreationForm()

    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(
                request,
                'Kayıt başarılı.'
            )
            return redirect('/calisanlar')

    return render(request, 'yeni_calisan.html',
                  {
                      'title' : 'Yeni Çalışan',
                      'form': form
                  }
            )

def yeni_rapor(request):
    form = SalesSlipCreationForm()

    if request.method == 'POST':
        form = SalesSlipCreationForm(request.POST)
        if form.is_valid():
            form.data.user_id = 2
            form.save()
            messages.info(
                request,
                'Kayıt başarılı.'
            )
            return redirect('/raporlar')
    return render(request, 'yeni_rapor.html',
                  {
                      'title' : 'Yeni Rapor',
                      'form': form
                  }
            )
    #
    #
    # return render(request, 'genel_rapor.html',
    #     {
    #         'form' : form,
    #         'title' : 'Genel Rapor',
    #     }
    # )


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(kullanici_adi = request.POST["kullanici_adi"],parola = request.POST["parola"])
            if user != None:
                request.session['user_id'] = user.id
                request.session['user_name'] = user.kullanici_adi
                return redirect('/')
            else:
                return redirect('login.html')
    return render(request, 'login.html',
            {
                'form': form
    })


def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(
                request,
                'Kayıt başarılı.'
            )
            return redirect('/login')
    return render(request, 'register.html',
                  {
                      'title' : 'Kayıt Ol',
                      'form' : form,
                  }
            )
def logout(request):
    request.session['user_id'] = None
    request.session['user_name'] = None
    return redirect('/login')