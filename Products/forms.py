from django.forms import ModelForm
from .models import Phone

class Phone_form(ModelForm):
    class Meta:
        model=Phone
        fields='__all__'

class Phone_edit_form(ModelForm):
    class Meta:
        model=Phone
        fields=[
            'title',
            'price',
            'quantity_available',
            'Battery',
            'RAM',
            'Storage'
        ]