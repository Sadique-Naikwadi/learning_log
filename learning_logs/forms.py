from django import forms
from django.forms.models import ModelForm
from . models import Topic, Entry

class TopicForm(forms.ModelForm):

    class Meta:

        model = Topic
        fields = ['title']
        labels = {'title': ''}

    
class EntryForm(forms.ModelForm):
    """Form definition for Entry."""

    class Meta:
        """Meta definition for Entryform."""

        model = Entry
        fields = ('text',)
        lables = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'col': 80})}

