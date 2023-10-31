# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... your other URL patterns ...
    path('add-product/', views.add_product, name='add_product'),
]
