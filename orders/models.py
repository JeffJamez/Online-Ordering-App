from django.db import models
from products.models import Item
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.
class OrderItem(models.Model):     # the shopping cart
    item = models.ForeignKey(Item, on_delete=models.CASCADE)     # relationship with item model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):          # to link all ordered items (shopping cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)        # to add the order items into the order table
    start_date = models.DateTimeField(auto_now_add=True)    # date the order was created
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total

    



