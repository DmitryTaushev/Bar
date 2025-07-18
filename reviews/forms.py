from django import forms
from reviews.models import Review
from users.forms import StyleFormMixin

class ReviewAdminForm(StyleFormMixin,forms.ModelForm):
    title = forms.CharField(max_length=150, label='Заголовок')
    content = forms.CharField(max_length=150,label='Содержимое')
    slug = forms.SlugField(max_length=20, initial='temp_slug', widget=forms.HiddenInput())

    class Meta:
        model = Review
        fields = ('title','content','slug')