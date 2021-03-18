from django.contrib import admin
from .models import *

class AdImageInline(admin.TabularInline):
    model = AdImage
    fields = ('image', 'description')
    max_num = 10
    min_num = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [AdImageInline,]


class AdItemInline(admin.TabularInline):
    model = CartItem
    fields = ('book', 'quantity')
    min_num = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [AdItemInline,]

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Review)
admin.site.register(Rating)
# admin.site.register(Star)
admin.site.register(Favorite)