from django import forms
from .models import Item, Inventory


class ItemForm(forms.Form):
    item_name = forms.CharField(label='Item Name', max_length=100)
    item_description = forms.CharField(label='Item Description', widget=forms.Textarea)
    item_quantity = forms.IntegerField()
    #Files are complicated - gonna implement this later
    #item_picture = forms.ImageField

    class Meta:
        model = Item
        fields = ['name', 'description', 'quantity', 'picture']
    