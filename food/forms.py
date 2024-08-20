from django import forms
from .models import items

class addItemForm(forms.ModelForm):
    class Meta:
        model = items
        fields = '__all__'

        # widgets = {
        #     'item_name' : forms.CharField(attrs={'class':'form-control', 'placeholder':'Product Name'}),
        #     'item_desc' : forms.CharField(attrs={'class':'form-control', 'placeholder': 'Product Description'}),
        #     'item_price' : forms.IntegerField(attrs={'class': 'form-control', 'placeholder': 'Product Price'}),
        #     'item_image' : forms.CharField(attrs={'class':'form-control', 'placeholder': 'Image URL'}),
        # }