from django.contrib import admin

# Register your models here.

from .models import Jackson

admin.site.register(Jackson)

from .models import BlogPost

admin.site.register(BlogPost)
