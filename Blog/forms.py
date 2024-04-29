from django import forms
from .models import *

class ListForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Blog başlığı giriniz..'}), required=False)
    description = forms.CharField( max_length=1000, required=False)
    date = forms.DateField(required=False)
    enddate = forms.DateField( required=False)
    release_status = forms.CharField(max_length=100, required=False)
    image=forms.ImageField(required=False)



    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("date")
        end_date = cleaned_data.get("enddate")
        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("Bitiş tarihi başlangıç tarihinden önce olamaz.")

    

   
  