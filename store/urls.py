from store import views
from django.urls import path
from .views import *
app_name = "store"

urlpatterns = [path("",views.homeview,name="homeview"),
               path("produits/home.html",views.homeview,name="homeviewFromProduits"),
               path("register/store/home.html",views.homeview,name="homeviewFromLogin"),
               path("produits/",views.index,name="index"),
               path("store/produits/",views.index,name="index"),
               path("register/", views.register, name="register"),
               path("login/", views.userlogin, name="login"),
               path("store/login/", views.userlogin, name="login2"),
               path('register/store/login',views.userlogin, name="login3"),
               path('login/store/register',views.register, name="register2"),
               path('register/store/store/register',views.register, name="register3"),
               path('detail/<int:id>',views.detail, name="detail"),
               path("logout/", views.logout, name="logout"),
               path("store/logout/", views.logout, name="logout2"),
               path("store/store/logout/", views.logout, name="logout2"),
               path("store/store/store/logout/", views.logout, name="logout3"),
               path("detail/store/showCart/store/store/store/store/logout", views.logout, name="logout4"),
               path("store/produits/store/showCart/store/store/store/logout", views.logout, name="logout5"),
               path("addToCart/", views.addToCart, name="addToCart"),
               path("showCart/", views.showCart, name="showCart"),
               path("detail/store/showCart/", views.showCart, name="showCart2"),
               path("store/produits/store/showCart/", views.showCart, name="showCart3"),
               path("checkout/", views.checkout, name="checkout"),
               path("detail/store/showCart/store/checkout", views.checkout, name="checkout2"),
               path("dashboard", views.dashboard, name="dashboard"),
               path("store/dashboard", views.dashboard, name="dashboard2"),
               path("detail/store/showCart/store/store/dashboard", views.dashboard, name="dashboard3"),
               path("store/produits/store/showCart/store/dashboard", views.dashboard, name="dashboard4"),
               path("orders", views.orders, name="orders"),
               path("store/orders", views.orders, name="orders"),
               path("store/store/orders", views.orders, name="orders2"),
               path("detail/store/showCart/store/store/store/orders", views.orders, name="orders3"),
               path("store/produits/store/showCart/store/store/orders", views.orders, name="orders4"),

              

               ]
#urlpatterns = [path("",views.index)]