from django.contrib import admin
from .models import Category, Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image', 'video', 'description')
    readonly_fields = ('slug',)

admin.site.register(Category)
admin.site.register(Movie, MovieAdmin)