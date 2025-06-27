import datetime
from django import forms

from menu.models import Category,DrinkAndDish
from users.forms import StyleFormMixin

class CategoryForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('owner', 'is_active', 'views')

class DrinkAndDishForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = DrinkAndDish
        exclude = ('owner', 'is_active', 'views')