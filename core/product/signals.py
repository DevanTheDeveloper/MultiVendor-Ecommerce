from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, Stock
from order.models import OrderItem


@receiver(post_save, sender=Product)
def productStock(sender,instance,created, **kwargs):
    if created:
        Stock.objects.create(product=instance)



@receiver(post_save, sender=OrderItem)
def StockUpdate(sender,instance,created, **kwargs):
    if created:

        productStock = instance.product.stock
        productStock.units -= instance.quantity
        productStock.units_sold += instance.quantity
        productStock.save()

