

from django.urls import path
from .views import *



urlpatterns = [
   path('',index,name='index'),
   path('movie/<int:id>/',movie,name='movie'),
   path('movie-detail/<slug:f_slug>/',movieDetay,name='detay'),
   path('search/',search,name='search'),
   
]
