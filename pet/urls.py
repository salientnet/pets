"""pet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
	url(r'^$', views.PetList.as_view(), name='pet_list'),
	url(r'^create$', login_required(views.PetCreate.as_view()), name='pet_create'),
	url(r'^(?P<pk>[0-9]+)/$', login_required(views.PetDetail.as_view()), name='pet_detail'),
	url(r'^(?P<pk>[0-9]+)/edit/$', login_required(views.PetUpdate.as_view()), name='pet_edit'),
	url(r'^(?P<pk>[0-9]+)/delete/$', login_required(views.PetDelete.as_view()), name='pet_del'),
]
