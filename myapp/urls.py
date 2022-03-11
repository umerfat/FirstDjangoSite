from django.contrib import admin
from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [

    # index given in url after http://127.0.0.1:8000/ will route to index view defined in views.py
    #path('index', views.index, name='index'),
    
    # removed index from above line so that by default url redirects to index view.
    path('', views.index, name='index'),
    #path('products/',views.products, name='products'),
    path('book/<int:book_id>/', views.detail, name='detail'),
    path('add/', views.addBook, name='add_book'),
    path('edit/<int:book_id>/', views.editBook, name='edit_book'),
    path('delete/<int:book_id>/', views.deleteBook, name='delete_book'),
]
