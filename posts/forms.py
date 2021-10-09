from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Share something new today...','rows':4, 'class':'shadow', 'style':'broder: none; border-radius: 10px;'}))

    image = forms.ImageField(label='', required=False, widget=forms.FileInput(attrs={'class':'form-control shadow mt-3 d-none', 'id':'file', 'onchange':'preview_image(event)'}))

    class Meta:
        model = Post
        fields = ('content', 'image')