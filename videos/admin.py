from django.contrib import admin

from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'status','created',)
    list_filter = ('status','updated',)
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Video, VideoAdmin)