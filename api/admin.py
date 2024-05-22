from django.contrib import admin
from .models import New

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title']

admin.site.register(New, NewsAdmin)
