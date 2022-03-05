from django.conf.urls import url

from django.contrib.auth.views import index
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
 
from . views import index


urlpatterns = [
    url(r'^index/$', index,
        name='index'),
  
   url(r'^counter/$', counter,
        name='counter'),
]
