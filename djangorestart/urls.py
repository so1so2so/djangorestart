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
from django.contrib import admin
from review import views
from django.conf.urls import include, url
import debug_toolbar
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^student/$', views.student,name='student'),
    url(r'^allclass/$', views.Allclass, name='allclass'),
    url(r'^allclass2/$', views.Allclass2, name='allclass2'),
    url(r'^teacher/$', views.teacher, name='teacher'),
    url(r'^teacher_add/$', views.teacher_change, name='teacher_change'),
    url(r'^test_all/$', views.Allclass, name='Allclass'),
    url(r'^login/$', views.login, name='login'),
    url(r'^teacher2/$', views.teacher2, name='teacher2'),
    url(r'^__debug__/', include(debug_toolbar.urls)),
]
