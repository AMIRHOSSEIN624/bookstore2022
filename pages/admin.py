from django.contrib import admin
from .models import Book,Comment


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', )


admin.site.register(Book, BookAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'datetime',)


admin.site.register(Comment, CommentAdmin)
