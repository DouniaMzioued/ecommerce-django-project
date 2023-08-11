from django.shortcuts import  render, redirect
from django.contrib.auth import login,authenticate,logout

from store.models import Cart, Customer, Order, Produit, order_detail
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q 
#Q for && and || 
def index(request):
    
    # produits = Produit.objects.get(id=8)
    produits = Produit.objects.all()

    context = {'produits': produits}
    return render(request,'index.html',context)
#a home function to redirect to 
def homeview(request):

    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # create a new User object with the form data
            user = User.objects.create_user(
                form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            user.save()
								
            # create a new Customer object with the form data and link it to the user
            customer = Customer(
                user=user,
                email=form.cleaned_data['email'],
                FirstName=form.cleaned_data['first_name'],
                LastName=form.cleaned_data['last_name'],
                phoneNumber=form.cleaned_data['phone_number'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],

                
                                )
            customer.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('store:homeview')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            request.session['username']=username
            # login(request, user)
            print("you are",request.session.get('username'))
            return redirect('store:homeview')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
def detail(request,id):
    totalitem=0
    produit = Produit.objects.get(id=id)
    item_already_in_cart = False
    

    if request.session.has_key('username'):
        username = request.session['username']
        totalitem = len(Cart.objects.filter(username=username))
        item_already_in_cart=Cart.objects.filter(Q(produit=produit.id) & Q(username=username)).exists()
        customer=Customer.objects.filter(username=username)
        for c in customer:
            name=c.FirstName,
        context ={
            "produit" : produit,
            "item_already_in_cart" : item_already_in_cart,
            "name" : name,
            "totalitem" : totalitem ,
        }
        return render(request,"produitDetail.html",context)
def logout(request):
    if request.session.has_key('username'):
        del request.session["username"]
        return redirect('store:login')
    else: 
        return redirect('store:login')
########################## C A R T ############################""
def addToCart(request):
    username = request.session['username']
#prod_id de lhtml du detail produit
    produit_id = request.GET.get('prod_id')
 
    produit=Produit.objects.filter(id=produit_id)
    produit_instance = produit.first()
    customer_id=Customer.objects.filter(username=username)
    customer_instance = customer_id.first()


    for p in produit:
        
        price = p.price
        Cart(price=price,username=username,customer=customer_instance,produit=produit_instance).save()
        return redirect(f"/store/detail/{produit_id}")

def showCart(request):
    totalitem=0
    if request.session.has_key('username'):
        username = request.session['username']
        totalitem = len(Cart.objects.filter(username=username))
        
        customer=Customer.objects.filter(username=username)
        for c in customer:
            name=c.FirstName,
            
            cart = Cart.objects.filter(username=username)


            context = {
            
             "name" : name,
             "totalitem" : totalitem ,
              "cart" : cart

            }
            if cart:
                
                return render (request,"showCart.html",context)
            else:

                return render (request,"emptyCart.html")



# dashboard

def dashboard(request):
    return render(request,"dashboard.html")
def orders(request):
    orders=Order.objects.filter(username=request.session['username']).order_by('-id')
    return render(request,"orders.html",{"orders":orders})

def checkout(request):
    #   if request.session.has_key('username'):
    #     if request.method == 'POST':

    #         username = request.session['username']
    #         name = request.POST.get("name")
    #         address = request.POST.get("address")
    #         phone = request.POST.get("phone")
            
    #         cart = request.session.get("cart")
    #         cart_product_id = list(cart.keys())
    #         products = Produit.get_products_by_id(cart_product_id)
    #         print(address, phone, username, cart, products)
    #         return redirect("store:showCart")
    #     else:
    #         return render(request, 'homeview.html')

    if request.session.has_key('username'):
        username = request.session['username']
        name = request.POST.get('name')
        adress = request.POST.get('adress')
        phone = request.POST.get('phone')
        
        cart_product=Cart.objects.filter(username=username)
        
        for c in cart_product:
            customer=c.customer
            price=c.price
            Order(totalPrice=price,username=username ,customer=customer).save()
       
            cart_product.delete()

        # print(name,adress,phone)
        return render (request,"showCart.html")
    else:
        return redirect('store:login')