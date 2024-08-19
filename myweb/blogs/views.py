from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def blogs(request):
    template = loader.get_template('myblogs.html')
    return HttpResponse(template.render())