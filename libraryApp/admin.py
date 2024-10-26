from django.contrib import admin
from .models import Students,Books,Library

# Register your models here.

admin.site.register(Students)
admin.site.register(Books)
admin.site.register(Library)