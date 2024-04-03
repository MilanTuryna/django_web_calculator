from django.shortcuts import render
from .forms import TriangleForm, SquareForm, CircleForm


def index(request):
    return render(request, "index.html")

def triangle(request):
    if request.method == 'POST':
        form = TriangleForm(request.POST)
        if form.is_valid():
            perimeter = form.calculate_perimeter()
            area = form.calculate_area()
            return render(request, 'triangle.html', {'form': form, 'perimeter': perimeter, 'area': area})
    else:
        form = TriangleForm()
    return render(request, 'triangle.html', {'form': form})

def square(request):
    if request.method == 'POST':
        form = SquareForm(request.POST)
        if form.is_valid():
            perimeter = form.calculate_perimeter()
            area = form.calculate_area()
            return render(request, 'square.html', {'form': form, 'perimeter': perimeter, 'area': area})
    else:
        form = SquareForm()
    return render(request, 'square.html', {'form': form})

def circle(request):
    if request.method == 'POST':
        form = CircleForm(request.POST)
        if form.is_valid():
            perimeter = form.calculate_perimeter()
            area = form.calculate_area()
            return render(request, 'circle.html', {'form': form, 'perimeter': perimeter, 'area': area})
    else:
        form = CircleForm()
    return render(request, 'circle.html', {'form': form})