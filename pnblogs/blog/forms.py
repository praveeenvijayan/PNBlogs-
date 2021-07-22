# from PIL import Image
from django import forms
from django.forms import fields, widgets
from . models import Post, Category

choices = Category.objects.all().values_list('name','name')

class addPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'thumbnail','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput({'class': 'form-control','enctype': 'multipart/form-data'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class editPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'thumbnail', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
