from django.http import HttpResponse
import forms
from django.shortcuts import redirect, render_to_response
import logging
from models import Snippet

def index(request):
    """Index page. Renders the form and last snippets in GET request,
    saves the form otherwise."""

    message = ''
    errors = {}

    if request.method == 'POST':
        form = forms.SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Snippet is saved'
        else:
            message = 'Form is invalid'
            return render_to_response('index.html', {
                'form': form,
                'message': message,
            })

    form = forms.SnippetForm()
    snippets = Snippet.objects.all()
    return render_to_response('index.html', {
        'form': form,
        'message': message,
        'snippets': snippets
    })
