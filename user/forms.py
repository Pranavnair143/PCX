from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.forms import TextInput,NumberInput

from .models import UserProfile

class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=20,help_text='Username',label='PCX Username :',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    email=forms.EmailField(max_length=200,label= 'Email :',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    first_name=forms.CharField(max_length=100,help_text='First Name',label='First Name :',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}))
    last_name=forms.CharField(max_length=100,help_text='Last Name',label='Last Name :',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}))
    
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].label='Enter Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label='Confirm Password'
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['mobile','address','city','district','state']
        widgets={
            'mobile':NumberInput(attrs={'class':'form-control','placeholder':'Mobile number'}),
            'address':TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'city':TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'district':TextInput(attrs={'class':'form-control','placeholder':'District'}),
            'state':TextInput(attrs={'class':'form-control','placeholder':'State'}),
        }