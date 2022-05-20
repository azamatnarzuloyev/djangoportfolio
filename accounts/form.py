from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CostumUser

class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model  = CostumUser
        fields = ('username','first_name','last_name','email','age')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model  = CostumUser
        fields = ('username','first_name','last_name','email','age')