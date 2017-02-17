from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('menu','category','maker','city','city_detail', 'text','dated_date')