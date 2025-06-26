import datetime
from django import forms

from drinks.models import Drink
from users.forms import StyleFormMixin

class DrinkForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Drink
        exclude = ('owner', 'is_active', 'views')