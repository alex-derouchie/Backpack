from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

#######################################################################
# This file defines the database models for the inv_manage app.
#######################################################################

#database representation of invantories
class Inventory(models.Model):
    name = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now_add = True)
    inv_size = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inv_manage-detail', kwargs={'pk': self.pk})


#Database representation of items
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    picture = models.ImageField(default='item_pics/default.png', upload_to='item_pics')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    #optional
    price = models.FloatField(default=0, blank=True)
    storage_location = models.CharField(max_length=100, default='', blank=True)
    status = models.CharField(max_length=100, default='', blank=True)
    internal_id = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('inv_manage-item-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

#Database model required to support inventory sharing
class SharePass(models.Model):
    added_user = models.ForeignKey(User, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    can_edit = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.added_user.username} <-> {self.inventory}"

