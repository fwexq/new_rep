
from django.forms import ModelForm, TextInput, Textarea, ImageField
from .models import *

class pictureForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Ничего не выбрано'

    class Meta:
       model = picture
       fields = ['title', 'opisanie', 'photo', 'cat']

       widgets = {
           "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
           "opisanie": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),

}


