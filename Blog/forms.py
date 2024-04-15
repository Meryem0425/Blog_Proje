from django import forms
from .models import *

class ListForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Blog başlığı giriniz..'}), required=False)
    description = forms.CharField(label='Description', max_length=1000, required=False)
    date = forms.DateField(label='Start Date', required=False)
    enddate = forms.DateField(label='End Date', required=False)
    release_status = forms.CharField(label='Release Status', max_length=100, required=False)

    class meta:
        model=arama
        fields=['name','description','date','enddate','release_status']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("date")
        end_date = cleaned_data.get("enddate")
        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("Bitiş tarihi başlangıç tarihinden önce olamaz.")


   
  