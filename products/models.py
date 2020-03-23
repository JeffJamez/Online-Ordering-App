from django.db import models
from django.shortcuts import reverse

# Create your models here.
CATEGORY_CHOICES = (             # creating categories of uniforms
    ('B', 'boys'),
    ('G', 'girls')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    price = models.FloatField()
    slug = models.SlugField()
    description = models.TextField(default='This is my description')
    image = models.ImageField(default='images.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:product-page", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("orders:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("orders:remove-from-cart", kwargs={
            'slug': self.slug
        })

