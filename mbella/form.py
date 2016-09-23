from django.forms import (
        ModelForm, HiddenInput, ValidationError
)

from mbella.models import (
        Customer,Employee,Services,Category,Sales_Slip,Sales_Slip_Action, User
)
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomerCreationForm(ModelForm):
    class Meta:
        model = Customer
        fields = (
            'admin',
            'ad_soyad',
            'dogum_tarihi',
            'eklenme_tarihi',
        )


class EmployeeCreationForm(ModelForm):
    class Meta:
        model = Employee
        fields = (
            'ad_soyad',
            'dogum_tarihi',
        )


class ServicesCreationForm(ModelForm):
    class Meta:
        model = Services
        fields = (
            'kategoriler',
            'hizmet_ismi',
            'hizmet_detayi',
            'hizmet_fiyati',
        )


class CategoryCreationForm(ModelForm):
    class Meta:
        model = Category
        fields = (
            'kategori_ismi',
        )


class SalesSlipCreationForm(ModelForm):
    class Meta:
        model = Sales_Slip
        fields = (
            'calisanlar',
            'musteriler',
            'kasa_fisi_zamani',
        )


class SaleSlipActionCreationForm(ModelForm):
    class Meta:
        model = Sales_Slip_Action
        fields = (
            'hizmetler',
            'kasa_fisi_zamani',
            'is_paid',
        )

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = (
            "kullanici_adi",
            "mail",
            "parola"

        )

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields =(
            'kullanici_adi',
            'parola',
        )
    # username = forms.CharField(required=True)
    # password = forms.CharField(widget=forms.PasswordInput,required=True)
    #
    # def clean(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #
    #     if not username or not password:
    #         return self.cleaned_data

        # user = authenticate(username=username, password=password)
        #
        # if user:
        #     self.user=user
        # else:
        #     raise ValidationError("Yanlış Kullanıcı adı veya şifre !")

        # return self.cleaned_data