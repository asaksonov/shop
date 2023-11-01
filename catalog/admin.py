from django.contrib import admin

from catalog.models import Category, Product
from blog.models import Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    ordering = ('pk',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'is_active')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    ordering = ('pk',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', 'is_published', 'views_count')
    ordering = ('pk',)