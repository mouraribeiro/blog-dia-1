from django.contrib import admin
from .models import Post


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'status', 'created_at')
    list_filter = ("status",)
    search_fields = ['titulo']


admin.site.register(Post, PostAdmin)
