from django.contrib import admin
from django.db import models
from AdminApp.models import Category,Cake
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
      list_display=("id","cat_name")
class CakeAdmin(admin.ModelAdmin):
      list_display=("id","cname","cake_image","price","description","category")
admin.site.register(Category,CategoryAdmin)
admin.site.register(Cake,CakeAdmin)