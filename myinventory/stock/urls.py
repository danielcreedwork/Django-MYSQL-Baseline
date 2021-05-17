"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views
app_name = 'stock'
urlpatterns = [
# Home page
path('', views.index, name='index'),
# Page that shows all topics.
path('types/', views.types, name='types'),
# Detail page for a single type.
path('types/<int:type_id>/', views.type, name='type'),
]