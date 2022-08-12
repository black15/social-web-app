from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
   password1 = forms.CharField(label='Password', max_length=250, required=True, widget=forms.PasswordInput)
   password2 = forms.CharField(label='Repeat Password', max_length=250, required=True, widget=forms.PasswordInput)

   class Meta:
      model    = User
      fields   = ('username', 'email', 'first_name')

   def c_password2(self):
      cd = self.cleaned_data
      if cd['password1'] != cd['password2']:
         raise forms.ValidationError('Password didn\'t match')
      return cd['password1']

class LoginForm(forms.Form):
   username = forms.CharField(label="Username", max_length=50, required=True)
   password = forms.CharField(label='Password', max_length=250, required=True, widget=forms.PasswordInput)
