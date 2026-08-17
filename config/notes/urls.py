from django.urls import path
from setuptools.extern import names

from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path("note/<int:pk>/", views.note_detail, name = "note_detail"),
    path('create/', views.note_created, name = 'note_create'),
    path('note/<int:pk>/edit', views.note_edit, name = 'note_edit')
]