from django.contrib import admin
from .models import Profile, Majlis, Tag

# Register your models here.
admin.site.register(Profile)
admin.site.register(Majlis)
admin.site.register(Tag)
