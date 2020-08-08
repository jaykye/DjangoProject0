from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta: # 아마도 overwriting일 것.
        model = Product
        fields =[
            'title',
            'description',
            'price',
        ]

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()

    def clean_title(self, *args, **kwargs): # this is 기본 함수, 내가 overwirte한 것.
        print("Clean_title function called")
        title = self.cleaned_data.get("title")
        if not 'title' in title:
            raise forms.ValidationError("Hey this is not valid.")
        else:
            return title
        print('clean title called.')