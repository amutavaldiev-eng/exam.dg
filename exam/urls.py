from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page),
    path('create_author/', create_author, name='create_author'),
    path('see_author/', see_author, name='see_author'),
    path('update_author/<int:id>/',update_author, name='update_author'),
    path('delete_author/<int:id>/',delete_author, name='delete_author'),
    path('update_books/<int:id>/',update_books, name='update_books'),
    path('delete_books/<int:id>/',delete_books,name='delete_books'),
    path('create_books/', create_books, name='create_books'),
    path('see_books/', see_books, name='see_books'),
    path('create_order/', create_order, name='create_order'),
    path('see_order/', see_order, name='see_order'),
    path('update_order/<int:id>/',update_order,name='update_order'),
    path('delete_order/<int:id>/',delete_order,name='delete_order') 
]