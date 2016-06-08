from django.conf import settings
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_shop_list(self):
        shop_list = Shop.objects.filter(categories=self)
        return shop_list

    def __str__(self):
        return self.title

class Shop(models.Model):
    title = models.CharField(max_length=20)
    contact_num = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    description = models.TextField()
    first_photo = models.ImageField()
    second_photo = models.ImageField(blank=True)
    third_photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    categories = models.ForeignKey('Category')

    def __str__(self):
        return self.title

class Review(models.Model):
    shop = models.ForeignKey('Shop')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.TextField()
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.comment