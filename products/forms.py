from django import forms
from .models import Product
class RawProductForm(forms.ModelForm):
    title2s       =forms.CharField()
    class Meta:
        model=Product
        fields=["title","description","price"]

    def clean_title(self,*args,**kwargs):
        title=self.cleaned_data.get("title")
        # if not "" in title:
        #     raise forms.ValidationError("This is not a FCB titlesn")
        return title
