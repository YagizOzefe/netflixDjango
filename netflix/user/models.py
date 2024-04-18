from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Abstrack user kullanıyorsak, migrate etmeden önce veri tabanımızı dosyadan silmeliyiz.
class CustomUser(AbstractUser):
    birth_date = models.DateField(null = True,blank = True)
    phone = models.CharField(max_length = 11)
    
    def profil_sayac(self):
        return self.profil_set.all().count()
    
    


class Profil(models.Model):
    title = models.CharField(max_length = 20)
    image = models.ImageField(upload_to='profil-resim') # Eklenen fotoğrafın nereye kayıt olacağı
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
