from django import forms
from django.conf import settings
from .models import Tweet

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH 
class TweetForm(forms.ModelForm):
   
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_Content(self):
        content = self.cleaned_data.get("Content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This content is too long")
        return content

    
