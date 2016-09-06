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
     home, musteriler, calisanlar, hizmetler,raporlar,genel_rapor
)
from profiles.views import (
    login, logout, register
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^login/', login, name="login"),
    url(r'^logout$', logout, name="logout"),
    url(r'^register/', register, name="register"),
    url(r'^musteriler$', musteriler, name="müşteriler"),
    url(r'^calisanlar$', calisanlar, name="çalışanlar"),
    url(r'^hizmetler$', hizmetler, name="çalışanlar"),
    url(r'^raporlar$', raporlar, name="çalışanlar"),
    url(r'^genel_rapor$', genel_rapor, name="çalışanlar"),

]

