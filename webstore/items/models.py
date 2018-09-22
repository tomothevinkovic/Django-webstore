from django.db import models
from webstore.settings import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    category_name = models.CharField(max_length = 100)
    targeted_audience = models.CharField(max_length = 50)
    category_pic = models.CharField(max_length = 1000)

    def __str__(self):
        return f"{self.category_name}"

class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    sub_name = models.CharField(max_length = 100)
    sub_pic = models.CharField(max_length = 1000)

    def __str__(self):
        return f"{self.sub_name}"


class Profile(models.Model):
    user = models.OneToOneField(User, related_name = 'profile', on_delete = models.CASCADE)
    city = models.CharField(max_length = 100, default = '')
    adress = models.CharField(max_length = 100, default = '')
    postalcode = models.CharField(max_length = 20, default = '')
    avg_rating = models.FloatField(default = 0)
    number_of_ratings = models.IntegerField(default = 0)
    total_rating = models.IntegerField(default = 0)
    
    def __str__(self):
        return f"{self.user.username}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Rating(models.Model):
    rated_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "rated_user", default = None)
    reviewer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "reviewer", default = None)
    rating = models.FloatField(default = 0)
    def __str__(self):
        return f"{self.reviewer} -> {self.rated_user}"

class Product(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = '')
    sub = models.ForeignKey(Sub_Category, on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 150)
    product_desc = models.CharField(max_length = 1000)
    product_price_value = models.CharField(max_length = 20)
    product_price_currency = models.CharField(max_length = 3, default = "USD")
    image1 = models.FileField(upload_to=f'media/products/images/', default = None)
    image2 = models.FileField(upload_to=f'media/products/images/', blank=True, null=True, default = None)
    image3 = models.FileField(upload_to=f'media/products/images/', blank=True, null=True, default = None)
    image4 = models.FileField(upload_to=f'media/products/images//', blank=True, null=True, default = None)
    image5 = models.FileField(upload_to=f'media/products/images/', blank=True, null=True, default = None)

    def __str__(self):
        return f"{self.product_name}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = '')
    product = models.ForeignKey(Product, on_delete = models.CASCADE, default = '')
    comment_text = models.CharField(max_length = 200, default = '')

    def __str__(self):
        return f"{self.comment_text}, ({self.user.username})"