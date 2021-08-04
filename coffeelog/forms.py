from django import forms
from django.db.models import fields
from .models import Log, Store

class LogForm(forms.ModelForm):
    
    class Meta:
        model = Log
        fields =(
            'store', 'product', 'price', 'hot' ,
            'bitter', 'acidity', 'smell' ,'after','likely','note')
        
        labels ={
            'store':'店名','product':'商品名','price':'価格',
            'hot':'hotならチェック','bitter':'苦味','acidity':'酸味','smell':'香り',
            'after':'後味','likely':'個人的な好み','note':'備考'}


class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ('name','address')
        labels = {'name':'店名', 'address':'住所(チェーン店ならチェーンと入力)'}
