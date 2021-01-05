from django import forms
from .models import Post, Images

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    public=forms.BooleanField(required=False)
 
    class Meta:
        model = Post
        fields = ('title', 'public', )
 
 
class ImageForm(forms.ModelForm):
    image = forms.ImageField()    
    class Meta:
        model = Images
        fields = ('image', )