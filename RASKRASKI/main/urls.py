from . import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
]
