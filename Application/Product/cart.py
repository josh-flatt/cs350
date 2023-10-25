# views.py
from django.shortcuts import render
from .models import CartItem

def list_products_in_cart(request):
    # Check if user is authenticated
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        return render(request, 'cart_list.html', {'cart_items': cart_items})
    else:
        # Redirect to login page or show a message
        return render(request, 'error.html', {'message': 'Please login to view your cart.'})
