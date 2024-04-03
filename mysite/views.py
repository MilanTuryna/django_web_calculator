from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

TEMPLATE_DIR = "templates/"

def index(request):
    return render(request, loader.get_template("index.html").render())

def circle(request):
    return render(request, TEMPLATE_DIR + 'circle.html')

def square(request):
    return render(request, TEMPLATE_DIR + 'square.html')

def triangle(request):
    return render(request, TEMPLATE_DIR + 'triangle.html')