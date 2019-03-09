"""Django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from app01 import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_classes',views.get_classes),
    url(r'^add_classes', views.add_classes),
    url(r'^update_classes', views.update_classes),
    url(r'^del_classes', views.del_classes),
    url(r'^get_students', views.get_students),
    url(r'^add_students', views.add_students),
    url(r'^update_students', views.update_students),
    url(r'^del_students', views.del_students),
    url(r'^get_teachers', views.get_teachers),
    url(r'^teacher_index', views.teacher_index),
    url(r'^add_teachers', views.add_teachers),
    url(r'update_teachers',views.update_teachers),
    url(r'del_teacher', views.del_teacher),
    url(r'give_classes', views.give_classes),
    url(r'remove_ajax', views.remove_ajax),
]
