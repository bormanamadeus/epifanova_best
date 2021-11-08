from django.contrib import admin

from .models import Clip, ClipTheme 

class ClipAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'file', 'published', 'cliptheme')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Clip, ClipAdmin)
admin.site.register(ClipTheme)

