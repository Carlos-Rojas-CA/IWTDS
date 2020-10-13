from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description')



# Register your models here.
admin.site.register(Books, BooksAdmin)