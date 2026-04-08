from django import forms
from api.models import product


class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ["id", "title", "content", "price"]
