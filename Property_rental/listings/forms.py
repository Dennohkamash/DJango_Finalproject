from django.forms import ModelForm
from .models import Listing

class listing_form(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        exclude  = ['created']