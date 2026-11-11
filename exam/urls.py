from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page),
    path('create_author/',create_author),
    path('see_author/',see_author),
    path('update_author/',update_author),
    path('delete_author/',delete_author),
    path('create_books/',create_books),
    path('see_books/',see_books),
    path('create_books/',create_books),
    path('create_books/',create_books),
    
]
