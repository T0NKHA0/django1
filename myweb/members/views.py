from django.shortcuts import render
from django.http import HttpResponse #เรียก Http มาใช้
from django.template import loader
# Create your views here.

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())
