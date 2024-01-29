from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Item(models.Model):

    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User, on_delete= models.CASCADE, default=1)
    item_name = models.CharField(max_length=100)
    item_intro = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=1000, default="https://static.wixstatic.com/media/bf242e_6133b4ae6a104cc2b50d70179f35efea~mv2.jpg/v1/fill/w_500,h_376,al_c,lg_1,q_80,enc_auto/food-placeholder.jpg")

    def get_absolute_url(self):
        return reverse("sizzleslice:detail", kwargs={"pk": self.pk})
