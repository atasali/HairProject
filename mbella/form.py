from django.forms import (
        ModelForm, HiddenInput, ValidationError
)

from mbella.models import (
        Customer,Employee,Services,Category,Sales_Slip,Sales_Slip_Action
)

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

