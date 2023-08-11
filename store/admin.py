from django.contrib import admin
from .models import Customer,Cart,Categorie,Payement,Produit,Visiteur,Order,order_detail


class CustomerAdmin(admin.ModelAdmin):
#     # list_display = ('id', 'title', 'date_sortie', 'qte_stock',
#     #                 'prix_location', 'categorie_id', 'date_creation')
    list_display = ("FirstName", "LastName", "email", "username", "password","phoneNumber","Adress")
    fields=('FirstName','LastName','email','username','password','phoneNumber','Adress')

    search_fields=('LastName','username')


# Register your models here.
admin.site.register(Cart)
admin.site.register(Categorie)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Payement)
admin.site.register(Produit)
admin.site.register(Visiteur)
admin.site.register(Order)
admin.site.register(order_detail)