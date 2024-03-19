from django.contrib import admin
from .models import User2, Product2, Order2, Author, Post


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_of_birth']
    list_filter = ['name', 'date_of_birth']
    search_fields = ['name', 'email']
    list_editable = ['date_of_birth']

    readonly_fields = ['email']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date', 'views']
    list_filter = ['author', 'date', 'views']
    search_fields = ['author__name', 'title']
    list_editable = ['author']

    readonly_fields = ['views']


@admin.register(User2)
class User2Admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date_registered']
    list_filter = ['name', 'date_registered']
    search_fields = ['name', 'email']
    search_help_text = 'Поиск по полям Имя(Name) и Email'
    list_editable = ['phone']

    readonly_fields = ['email']


@admin.register(Product2)
class Product2Admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount', 'date_added']
    list_filter = ['name', 'date_added']
    search_fields = ['name', 'description']
    search_help_text = 'Поиск по полям Имя(Name) и Описание(Description)'
    list_editable = ['amount']

    readonly_fields = ['photo']


@admin.register(Order2)
class Order2Admin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'date_ordered']
    list_filter = ['customer', 'date_ordered']
    search_fields = ['customer']
    search_help_text = 'Поиск по полю Покупатель(customer)'





