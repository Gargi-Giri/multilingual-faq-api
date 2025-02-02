from django.contrib import admin

# Register your models here.
from .models import FAQ  # Import the FAQ model

admin.site.register(FAQ)  # Register it with the admin panel
