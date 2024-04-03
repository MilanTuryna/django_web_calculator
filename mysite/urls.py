from django.contrib import admin
from django.urls import include, path

from shapes import views

urlpatterns = [
    path("", views.index),
    path("triangle/", views.triangle, name="triangle"),
    path("square/", views.square, name="square"),
    path("circle/", views.circle, name="circle"),
    path("admin/", admin.site.urls),
]