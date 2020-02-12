from django.forms import ModelForm
from .models import PeanutButter

class PeanutButterForm(ModelForm):
    class Meta:
        model = PeanutButter
        exclude = []
        # fields = ['brand']