from models import Snippet
from django.forms import ModelForm



"""
class SnippetForm(forms.Form):
    title = forms.CharField(max_length=100)
    filename = forms.CharField()
    code = forms.CharField(widget=forms.Textarea)
    lang = forms.CharField(max_length=30,
            widget=forms.Select(choices=LANG_CHOICES))
"""


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
