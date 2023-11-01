from django.contrib import admin
from .models import Product, Color, Size, Category, Like, Comment

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Comment)

