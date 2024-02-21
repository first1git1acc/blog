from django.contrib import admin
from .models import Post,Comment
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author'] #додає колонку із фільтрами для полів
    raw_id_fields = ['author'] #замість списку із юзерів створює поле пошуку юзера

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body'] #поля за якими можна здійснювати пошук