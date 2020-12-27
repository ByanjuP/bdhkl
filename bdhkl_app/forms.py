from django import forms
from .models import Post,Destinations
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostCreateForm(forms.ModelForm):
    body = forms.CharField(initial='Your name',widget=SummernoteWidget())
    featured_image = forms.ImageField(label='Upload  Featured Image')
    class Meta:
        model = Post
        fields = ['title','body','featured_image']

class DestinationForm(forms.ModelForm):
    body = forms.CharField(widget = SummernoteWidget())
    featured_image = forms.ImageField(label='Upload  Featured Image')

    class Meta:
        model = Destinations
        fields = ['title','body','featured_image']

