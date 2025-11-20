from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','muddat')
    list_filter = ('janr','year','rejissyor')
    search_fields = ('title',)
    
    


