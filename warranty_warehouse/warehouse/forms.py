from django import forms
from .models import Part

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['order', 'name', 'part_number', 'quantity', 'storage_location', 'status']
