from django.contrib import admin
from mbella.models import (
    User, Customer, Employee, Category, Services, Sales_Slip, Sales_Slip_Action,
)
from django.db import models

class UserAdmin(admin.ModelAdmin):
    list_display = ["kullanici_adi", "mail","is_active"]
    search_fields = ["kullanici_adi", "mail"]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["ad_soyad","dogum_tarihi"]
    search_fields = ["ad_soyad","dogum_tarihi"]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["admin","ad_soyad","dogum_tarihi", "eklenme_tarihi"]
    search_fields = ["admin","ad_soyad", "dogum_tarihi"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["kategori_ismi"]
    search_fields = ["kategori_ismi"]

class ServicesAdmin(admin.ModelAdmin):
    list_display = ["kategoriler","hizmet_ismi","hizmet_detayi", "hizmet_fiyati"]
    list_editable = ["hizmet_detayi"]
    search_fields = ["kategoriler","hizmet_ismi","hizmet_detayi", "hizmet_fiyati"]

class SalesSlipAdmin(admin.ModelAdmin):
    list_display = ["calisanlar","musteriler","kasa_fisi_zamani"]
    search_fields = ["calisanlar","musteriler"]

class SalesSlipActionAdmin(admin.ModelAdmin):
    list_display = ["hizmetler","kasa_fisi_zamani","is_paid"]
    search_fields = ["hizmetler", "kasa_fisi_zamani"]



admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Sales_Slip,SalesSlipAdmin)
admin.site.register(Sales_Slip_Action,SalesSlipActionAdmin)


# Register your models here.
