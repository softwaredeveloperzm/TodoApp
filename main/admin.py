from django.contrib import admin
from .models import Task  # Import the Tasks model

# Register the Tasks model
admin.site.register(Task)
