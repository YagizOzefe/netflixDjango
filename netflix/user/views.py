from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.contrib import messages
# Create your views here.

def user_login(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u_email = form.cleaned_data.get('email') # cleaned_data -> Bizim için string veri alıyor
            u_password = form.cleaned_data.get('password')
            u_username = CustomUser.objects.get(email = u_email).username
            user = authenticate(request, username=u_username,password=u_password) 
            #Formdan alınan email ve password ile kayıtlı olanlar eşleşiyorsa user değişkeninin içine bu bilgiyi atıcak.
            #Authenticate methodu bize burdaki kontrolü sağlayan yapı.
            if user is not None:

                login(request,user)
                messages.success(request,f'Giriş başarılı, Hoşgeldiniz {user.first_name.capitalize()}')
                return redirect('index')
            else:
                return render(request,'login.html',{'form':form})

    form = LoginForm()
    return render(request,'login.html',{'form':form})


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Kayıt başarılı')
            return redirect('login')
        else:
            messages.error(request,'Kayıt başarısız alanları kontrol ediniz')
            return render(request,'register.html',{'form':form})
    form = RegisterForm()
    return render(request,'register.html',{'form':form})
    


def user_logout(request):
    logout(request)
    return redirect('index')


def profil(request):
    
    if request.method == 'POST':
        #!
        profilId = request.POST['sil']
        profil = Profil.objects.get(id = profilId)
        profil.delete()
        messages.info(request,'Profil silme başarılı')
    else:
        
        return render(request,'profil.html')
    
    return render(request,'profil.html')


def profilManage(request):
   
    
    if request.method == 'POST':
        form = ProfilForm(request.POST,request.FILES) # Formdan bir image gönderiliyorsa 
        #request.POST un yanına request.FILES eklenmelidir.
        if form.is_valid():

            if request.user.profil_sayac() < 3:

                profil = form.save(commit=False)
                profil.owner = request.user
                profil.save()
                messages.success(request,'Profil Ekle Başarılı')
                return redirect('profil')
            else:
                messages.error(request,'En fazla 3 tane profil ekleyebilirsiniz.')
   
    form = ProfilForm()
   
    return render(request,'profil-manage.html',{'form':form})