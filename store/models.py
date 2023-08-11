from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
status_choices = (
        ('Accepted', 'Accepted'),
        ('Packed', 'Packed'),
        ('On the way', 'On the way'),
        ('Delivered', 'Delivered'),
        ('Cancel', 'Cancel'),
        ("Completed", "Completed"),
    )
class Visiteur(models.Model):
    estinscrit = models.BooleanField(default=0)


# class Client(models.Model):
#     user=models.OneToOneField(User, default="",on_delete=models.CASCADE)
#     firstname = models.CharField(max_length=60,default="" )
#     lastname = models.CharField(max_length=60,default="" )
    # Email = models.EmailField(unique=True, default="")
    # Adress = models.CharField(max_length=60,null=True)
    # City = models.CharField(max_length=60,null=True)
    # StateProvince = models.CharField(max_length=60,null=True)
    # phoneNumber = models.TextField(max_length=13,null=True)
    # username = models.CharField(max_length=60, default="")
    # password = models.CharField(max_length=20, default="")
   
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = [FullName,Email]


class Customer(models.Model):
    user=models.OneToOneField(User, default="",on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=60,default="" )
    LastName = models.CharField(max_length=60,default="" )
    email = models.EmailField(unique=True,default="" )
    Adress = models.CharField(max_length=60,null=True)
    City = models.CharField(max_length=60,null=True)
    StateProvince = models.CharField(max_length=60,null=True)
    phoneNumber = models.CharField(max_length=13,null=True)
    username = models.CharField(max_length=60, default="")
    password = models.CharField(max_length=20, default="")

   
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = [FullName,Email]
    # def __str__(self):
    #     return self.FirstName,self.LastName,self.email
class Categorie(models.Model):
    name = models.CharField(max_length=60, default="")
    def __str__(self):
        return self.name
#Static methods in Django are often used for utility functions
# that don't require access to any instance variables or methods of the class. They can be defined using the @staticmethod decorator.
    @staticmethod
    def getallcategories():
        return Categorie.objects.all()

class Produit(models.Model):
    name = models.CharField(max_length=60, default="")
    description = models.TextField(max_length=60, default="")
    price = models.FloatField(default=0)
    qteStock = models.IntegerField(default=0)
    image = models.CharField(max_length=1000, default="")
    category = models.ForeignKey(
        Categorie, default="", on_delete=models.CASCADE)
    def get_products_by_id(cart_product_id):
        return Produit.objects.filter(id__in=cart_product_id)


class Cart(models.Model):
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    username =  models.CharField(max_length=60, default="")
    quantity = models.PositiveIntegerField(default=1)
    
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.CASCADE)
    


class Order(models.Model):

    totalPrice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    OrderDate = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=60, default='Pending',choices=status_choices)
    username =  models.CharField(max_length=60, default="")
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)


class order_detail(models.Model):
    qte_produit = models.IntegerField(default=0)
    order = models.ForeignKey(Order, default="", on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, default="", on_delete=models.CASCADE)


class Payement(models.Model):
    credit_debit_card_number = models.TextField(default="")
    expiration_date = models.DateTimeField(default=timezone.now)
    security_code = models.IntegerField(default=0)
    billing_address = models.TextField(default="")
    order = models.ForeignKey(Order, default="", on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customer, default="", null=True, on_delete=models.CASCADE)
