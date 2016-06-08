from django import forms
from .models import Category, Shop

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
