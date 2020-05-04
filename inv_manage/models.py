from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Inventory(models.Model):
    name = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now_add = True)
    inv_size = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inv_manage-detail', kwargs={'pk': self.pk})


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    picture = models.ImageField(default='default.jpg', upload_to='item_pics')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    #optional
    price = models.FloatField(default=0, blank=True)
    storage_location = models.CharField(max_length=100, default='', blank=True)
    status = models.CharField(max_length=100, default='', blank=True)
    internal_id = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.name


    

