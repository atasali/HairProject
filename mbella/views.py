from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone

from .models import Customer, Employee, Services
from mbella.form import (
    CustomerCreationForm, EmployeeCreationForm, ServicesCreationForm, SalesSlipCreationForm, SaleSlipActionCreationForm
)

# Create your views here.

def home(request):
    customer = Customer.objects.all()
    return render(request, 'home.html',
        {
            'title': 'AnaSayfa',
        }
    )

def musteriler(request):
    form = CustomerCreationForm()

    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.info(
                request,
                'Kayıt başarılı.'
            )

            return redirect('/')

    return render(request, 'musteriler.html',
        {
            'form' : form
        }
    )


def calisanlar(request):
    form = EmployeeCreationForm()

    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.info(
                request,
                'Kayıt başarılı.'
            )
            return redirect('/')

    return render(request, 'calisanlar.html',
        {
            'form' : form
        }
    )


def hizmetler(request):
    form = ServicesCreationForm()

    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.info(
                request,
                'Kayıt başarılı.'
            )
            return redirect('/')

    return render(request, 'hizmetler.html',
        {
            'form': form
        }
    )

def raporlar(request):
    form = SalesSlipCreationForm()

    if request.method == 'POST':
        form = SalesSlipCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.info(
                request,
                'Kayıt başarılı.'
            )
            return redirect('/')

    return render(request, 'raporlar.html',
        {
            'form' : form
        }
    )

def genel_rapor(request):
    form = SaleSlipActionCreationForm()

    if request.method == 'POST':
        form = SaleSlipActionCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.info(
                request,
                'Kayıt başarılı.'
            )
            return redirect('/')

    return render(request, 'genel_rapor.html',
        {
            'form' : form
        }
    )
