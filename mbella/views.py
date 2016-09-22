from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import Customer, Employee, Services, Sales_Slip, Sales_Slip_Action
from mbella.form import (
    CustomerCreationForm, EmployeeCreationForm, ServicesCreationForm, SalesSlipCreationForm, SaleSlipActionCreationForm,
)
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request, Sales_Slip_Acton_id=1):
    salesslipactions = Sales_Slip_Action.objects.all()
    return render(request, 'home.html',
        {
            'title' : 'AnaSayfa',
            'salesslipactions' : salesslipactions,
        }
    )

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

