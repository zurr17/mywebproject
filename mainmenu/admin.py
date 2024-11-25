# main/admin.py
from django.contrib import admin
from .models import BookRental, ReviewSite, Contact, Merek, Motor, Peminjaman, Library, Product, Cart, Order


# admin.site.register(Library)
# admin.site.register(BookRental)
# admin.site.register(ReviewSite)

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

@admin.register(BookRental)
class BookRentalAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

@admin.register(ReviewSite)
class ReviewSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'rating', 'book_id')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

@admin.register(Merek)
class MerekAdmin(admin.ModelAdmin):
    pass

@admin.register(Motor)
class MotorAdmin(admin.ModelAdmin):
    pass


@admin.register(Peminjaman)
class PeminjamanAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Cart)
class CartItemAdmin(admin.ModelAdmin):
    list_display =[
        'product',
        'quantity',
        ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
# Register your models here.


