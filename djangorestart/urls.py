"""djangorestart URL Configuration

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
from review import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^student/$', views.student,name='student'),
    url(r'^allclass/$', views.Allclass, name='allclass'),
    url(r'^teacher/$', views.teacher, name='teacher'),
    url(r'^teacher_add/$', views.teacher_change, name='teacher_change'),
]
