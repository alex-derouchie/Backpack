from django.contrib import admin
from .models import Inventory, Item, SharePass

#######################################################################
# Registers database models with the admin site so they can be accessed
# there.
#######################################################################

admin.site.register(Inventory)
admin.site.register(Item)
admin.site.register(SharePass)
