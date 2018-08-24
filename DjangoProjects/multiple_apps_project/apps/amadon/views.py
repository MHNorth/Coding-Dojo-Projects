from django.shortcuts import render, redirect
from .models import Product, ProductCategorie



##----------------Amadon Store----------------##

catlist = ProductCategorie.objects.all()

def AmadonHome(request, *args, **kwargs):
        context = {
                'catlist': catlist
        }
        return render(request, 'amadon/amadonhome.html', context)  

def AmadonBuy(request, *args, **kwargs):
        if request.session:

                 if 'cart' not in request.session:
                        request.session['cart'] = []
      


        return redirect('amadonhome')

def AmadonDetail(request):
        return render(request, 'amadon/amadondetail.html')

def AmadonCheckout(request):

        def add_to_cart(product_id):
                if "cart" not in request.session:
                        request.session["cart"] = []
                        product_name = ""
        return render(request, 'amadon/amadoncheckout.html') 



