from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse, StreamingHttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest
from django.template.loader import get_template, render_to_string
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy

from django.views.generic.base import TemplateView, View

from .models import Clip, ClipTheme

def index(request, **kwargs):

    if 'theme_id' in kwargs: 
        clips = Clip.objects.filter(cliptheme=kwargs['theme_id'])
    else:
        clips = Clip.objects.all()

    themes = ClipTheme.objects.all()

    context = {'clips': clips, 'themes': themes}

    return render(request,'main_page_app/index.html', context)
