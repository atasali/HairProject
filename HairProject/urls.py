"""HairProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.static import serve
from mbella.views import (
     home, musteriler, calisanlar, hizmetler,raporlar,
     yeni_musteri, yeni_hizmet, yeni_calisan, yeni_rapor,
     login, register, logout
)
# from profiles.views import (
#     login, logout, register
# )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^login/', login, name="login"),
    url(r'^logout$', logout, name="logout"),
    url(r'^register/', register, name="register"),
    url(r'^musteriler$', musteriler, name="müşteriler"),
    url(r'^calisanlar$', calisanlar, name="çalışanlar"),
    url(r'^hizmetler$', hizmetler, name="hizmetler"),
    url(r'^raporlar$', raporlar, name="raporlar"),
    url(r'^yeni_musteri$', yeni_musteri, name="yeni_musteri"),
    url(r'^yeni_hizmet$', yeni_hizmet, name="yeni_hizmet"),
    url(r'^yeni_calisan$', yeni_calisan, name="yeni_calisan"),
    url(r'^yeni_rapor$', yeni_rapor, name='yeni_rapor')

]

