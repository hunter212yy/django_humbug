from django.contrib import admin

from .models import Post, Tag

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    list_filter = ('tags',)
    search_fields = ('post_title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)