from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'store/home.html')

def product_list(request):
    # Temporary sample products (we'll remove this later)
    products = [
        {
            'name': 'Red T-Shirt',
            'price': 599,
            'description': 'Soft and comfortable cotton shirt.',
            'image': 'https://via.placeholder.com/200x200?text=Red+T-Shirt'
        },
        {
            'name': 'Blue Jeans',
            'price': 999,
            'description': 'Classic slim-fit jeans.',
            'image': 'https://via.placeholder.com/200x200?text=Blue+Jeans'
        },
        {
            'name': 'White Sneakers',
            'price': 1499,
            'description': 'Stylish sneakers for everyday use.',
            'image': 'https://via.placeholder.com/200x200?text=White+Sneakers'
        }
    ]
    
    return render(request, 'store/product_list.html', {'products': products})
