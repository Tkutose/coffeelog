from django import forms
from .models import Log

class LogForm(forms.ModelForm):
    
    class Meta:
        model = Log
        fields =('store', 'product', 'price', 'hot' ,
                'bitter', 'acidity', 'smell' ,'after','likely','note')
