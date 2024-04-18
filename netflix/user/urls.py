

from django.urls import path
from .views import *



urlpatterns = [
   path('login/',user_login,name='login'),
   path('register/',user_register,name='register'),
   path('loguot/',user_logout,name='logout'),
   path('profil/',profil,name='profil'),
   path('profil-manage/',profilManage,name='profil-ekle'),
   
]
