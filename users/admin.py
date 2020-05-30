from django.contrib import admin
from .models import Profile

#######################################################################
# Registers database models with the admin site so they can be accessed
# there.
#######################################################################

admin.site.register(Profile)

