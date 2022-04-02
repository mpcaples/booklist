from django.contrib import admin
from .models import Book, Author, Publisher

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_filter = ("author", "my_rating", "is_bestseller",)
    list_display = ("title", "author",)

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Publisher)