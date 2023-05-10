import datetime

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import URL
from .forms import URLForm
import string
import random


def index(request):
    return render(request, 'shortener/index.html')


def about(request):
    return render(request, 'shortener/about.html')


def redirect_to_url(request, short_url):
    link = URL.objects.get(short_url=short_url)
    link.visits += 1
    link.save()
    return redirect(link.original_url)

def stats(request):
    links = URL.objects.all()
    return render(request, 'shortener/stats.html', {
        'links': links
    })

def add_link(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        link= URL.objects.filter(original_url=original_url).first()
        if link:
            return render(request,'shortener/link_added.html',{
                'original_url':link.original_url,
                'short_url':link.short_url
            })
        else:
            link = URL(original_url=original_url)
            link.save()
            return render(request, 'shortener/link_added.html', {
                'original_url': link.original_url,
                'short_url': link.short_url
            })





