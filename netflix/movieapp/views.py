from django.shortcuts import render,redirect
from .models import *
from user.models import *
from django.db.models import Q
# Create your views here.



def index(request):
    if request.user.is_authenticated:
        return redirect('profil')
    return render(request,'index.html')


def movie(request,id):
    profil = Profil.objects.get(id = id)
    profiller = request.user.profil_set.all()
    kategori = Category.objects.get(title = 'Komedi')
    komediFilmleri = Movie.objects.filter(category = kategori)
    #Databasedeki category ile istediğim kategoryi eşleşiyorsa çek
    print(kategori)
    filmler = Movie.objects.all()
    context = {
        'filmler':filmler,
        'profil':profil,
        'profiller':profiller,
        'id':id,
        'kategori':kategori,
        'komediFilm':komediFilmleri,
        
    }
    return render(request,'movie.html',context)



def movieDetay(request,f_slug):
    
    film = Movie.objects.get(slug = f_slug)
    print(film)
    context = {
        'film':film,
        #'deneme':f_slug,
    }
    return render(request,'movie-detail.html',context)


def search(request):
    tumFilmler = Movie.objects.all()
    if 'search' in request.GET and request.GET.get('search'):
   #Eğer 'search' anahatarı inputta varsa, kullanıcı bir arama yaptıysa, boş değilse
        cumle = request.GET.get('search')
        print(cumle)
        # inputun içindeki veriyi al ve 'cumle' değişkenine ata
        filmler = Movie.objects.filter(
            Q(title__icontains=cumle) |
            Q(description__icontains=cumle)
        ) # icontains = küçük büyük harf bakmadan eşle sağlanıyorsa filterelemyi gerçekleştirir
        
    context = {
        'filmler':filmler,
        'cumle':cumle,
        'tumFilmer':tumFilmler
    }
        
        
    return render(request,'search.html',context)
