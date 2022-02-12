from django.contrib import admin
from .models import owner
from .models import pet
admin.site.register(owner)
admin.site.register(pet)