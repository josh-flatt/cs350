# AI Learning for Milestone 4

Here are AI prompts and responses for Milestone 4, based on the tasks you provided:

## 1. Write Django code to Add Product to the database

To add a product to the database, you'll first need to create a model for the product:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
```

After creating the model and running migrations, you can add products using Django's ORM:

```python
new_product = Product(name="Sample Product", description="This is a sample product.", price=19.99)
new_product.save()
```

## 2. Write Django view code to Add Product

To create a view where users can add a product:

```python
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
```

And you'll need a corresponding form in `forms.py`:

```python
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
```

## 3. Write Django view code to List Products (in cart)

Assuming you have a model for a cart and cart items:

```python
def list_products_in_cart(request):
    cart = Cart.objects.get(user=request.user)  # Fetch the cart for the logged-in user
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart_products_list.html', {'cart_items': cart_items})
```

## 4. Paste an error message into ChatGPT

You can share any Django or Python-related error messages or logs with ChatGPT to get assistance in debugging and finding solutions.

## 5. Show how to log issues with Github

To log issues with GitHub:

1. Navigate to the main page of the repository on GitHub.
2. Click on the "Issues" tab.
3. Click the "New issue" button.
4. Fill in a descriptive title and provide detailed information about the issue in the description box.
5. Use labels, assignees, and other available fields as needed to categorize and delegate the issue.
6. Once you have filled in all the necessary details, click the "Submit new issue" button.

Remember to include relevant details in your issue description, such as steps to reproduce, expected behavior, actual behavior, and any error messages or logs.
