from django.shortcuts import render, HttpResponse, redirect, get_object_or_404    #check whether an object is found or raise a 404 error
from store.models import Category, Product, Customers

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render('request', 'store/index.html', context=user_dict)


def index(request):
    return render(request, "store/index.html")

def shop(request):
    product_list = Product.objects.order_by('category')
    category_dict = {'access_categ':product_list}
    return render(request, "store/shop.html")

def cart(request):
    return render(request, "store/cartitems.html")


def product_list(request, category_bldurl=None):      #used to display a list of products and allow users to filter via categories
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_bldurl:                                #optionally filter the products based on the category_bldurl parameter
        category = get_object_or_404(Category, bldurl=category_bldurl)
        products = Product.objects.filter(category=category)
 
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'store/product/shoplist.html', context)
 
 
def product_detail(request, id, bldurl):
    product = get_object_or_404(Product, id=id, bldurl=bldurl, available=True)
    context = {
        'product': product
    }
    return render(request, 'store/product/cartitems.html', context)