from django import forms
from .models import Item, Inventory

#######################################################################
# This file defines the form objects for the inv_manage app.
#######################################################################

# ItemForm uses a custom Form instead of a ModelForm so the inventory
# field can be filled automatically
class ItemForm(forms.Form):
    item_name = forms.CharField(label='Item Name', max_length=100)
    item_description = forms.CharField(label='Item Description', widget=forms.Textarea)
    item_quantity = forms.IntegerField()
    #Files are complicated - gonna implement this later
    #item_picture = forms.ImageField

class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['inventory']

#Form responsible for adding other users to one of the current users' inventories.
class ShareForm(forms.Form):
    user_to_add = forms.CharField(label="Add User", max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    user_access = forms.ChoiceField(label="User Access", choices=(("can_edit", "Can Edit"), ("can_view", "Can View")))
    