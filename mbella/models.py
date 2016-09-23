from django.db import models, IntegrityError
from django.conf import settings
from datetime import date, datetime
from django.utils import timezone
from django.conf.urls import url
from decimal import Decimal


class User(models.Model):
    kullanici_adi = models.CharField(max_length=255)
    parola = models.CharField( max_length=255)
    mail = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)


    def ekle(self):
        self.kullanici_adi
        self.save()

    def __str__(self):
        return self.kullanici_adi

    class Meta:
        verbose_name_plural = "Kullanıcılar"

# Müşteri bilgilerinin oluşturulduğu model
class Customer(models.Model):
    user = models.ForeignKey(User, null=True)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    ad_soyad = models.CharField(max_length=255)
    dogum_tarihi = models.DateField(null=True)
    eklenme_tarihi = models.DateTimeField(default=timezone.now())

    def ekle(self):
        self.eklenme_tarihi = timezone.now()
        self.save()


    def __str__(self):
        return self.ad_soyad

    class Meta:
        verbose_name_plural = "Müşteriler"


# Çalışanların bilgilerinin oluşturulduğu model
class Employee(models.Model):
    user = models.ForeignKey(User, null=True)
    ad_soyad = models.CharField(max_length=255)
    dogum_tarihi = models.DateField(null=True)
    #image = models.ImageField(upload_to="Employee")

    def __str__(self):
        return self.ad_soyad

    class Meta:
        verbose_name_plural = "Çalışanlar"


# Kategorilerin oluşturulduğu model
class Category(models.Model):
    user = models.ForeignKey(User, null=True)
    kategori_ismi = models.CharField(max_length=255)

    def __str__(self):
        return self.kategori_ismi

    class Meta:
        verbose_name_plural = "Kategoriler"


# Hizmet bilgilerinin oluşturulduğu model
class Services(models.Model):
    kategoriler = models.ForeignKey(Category, on_delete=models.CASCADE)
    hizmet_ismi = models.CharField(max_length=255)
    hizmet_detayi = models.CharField(max_length=255)
    hizmet_fiyati = models.DecimalField(max_digits=9, decimal_places=1)

    def __str__(self):
        return self.hizmet_ismi

    class Meta:
        verbose_name_plural = "Hizmetler"


# Satış fişi oluşturmak için kullanılan model
class Sales_Slip(models.Model):
    user = models.ForeignKey(User, null=True)
    musteriler = models.ForeignKey(Customer)
    calisanlar = models.ForeignKey(Employee)
    kasa_fisi_zamani = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return format(self.kasa_fisi_zamani)

    class Meta:
        verbose_name_plural = "Kasa Fişi"


# Satış fişindeki bütün aksiyonların bulunduğu model
class Sales_Slip_Action(models.Model):
    hizmetler = models.ForeignKey(Services, on_delete=models.CASCADE)
    kasa_fisi_zamani = models.ForeignKey(Sales_Slip, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    # is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return format(self.hizmetler)

    class Meta:
        verbose_name_plural = "Kasa Fişi Raporu"


