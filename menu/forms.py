import datetime
from django import forms

from menu.models import Category
from users.forms import StyleFormMixin

class CategoryForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('owner', 'is_active', 'views')