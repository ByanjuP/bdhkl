from django.contrib import admin
from .models import Post, Destinations, Gallery, Hotel,Thingstodo
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')

class DestinationsAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')

admin.site.register(Post,PostAdmin)
admin.site.register(Destinations,DestinationsAdmin)
admin.site.register(Gallery)
admin.site.register(Hotel)

@admin.register(Thingstodo)
class ThingstodoAdmin(admin.ModelAdmin):
    list_display = ['id','title','featured_image','body']




