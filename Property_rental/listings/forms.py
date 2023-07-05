from django.forms import ModelForm
from .models import Listing, User
from django.contrib.auth.forms import UserCreationForm

class listing_form(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        exclude  = ['created']
        
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        