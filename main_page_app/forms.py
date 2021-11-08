from django.forms import ModelForm

from .models import Clip

class ClipForm(ModelForm):
    class Meta:
        model = Clip
        fields ='__all__'
