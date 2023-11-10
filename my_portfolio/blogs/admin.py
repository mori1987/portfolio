from django.contrib import admin
from .models import Blogs

@admin.register(Blogs)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','image','content','date','slug')
    list_filter = ('date',)
    search_fields = ('title','content')
