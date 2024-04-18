from django import forms
from django.contrib.auth.forms import UserCreationForm  
from .models import *
from django.forms import widgets
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_email(self):
     userEmail = self.cleaned_data.get('email')
     if not CustomUser.objects.filter(email = userEmail).exists():
        self.add_error('email','Bu mail adresi kayıtlı değildir.')
     return userEmail


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email','birth_date','phone')
        #fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'birth_date' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control'}),
        }
        for field_name,widget in widgets.items():
            self.fields[field_name].widget = widget
    
    def clean_email(self):
        userEmail = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email = userEmail).exists():
            self.add_error('email','Bu mail adresi kullanılıyor.')
        return userEmail
    


class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ('title','image')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['image'].widget = widgets.FileInput(attrs={'class':'form-control'})
    

 

    