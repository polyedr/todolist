from django.contrib import admin
from . import models


class CommentInline(admin.TabularInline):
    model = models.Comment


class Todo_postAdmin(admin.ModelAdmin):
    fields = ('title', 'priority', 'body', 'is_ready')
    list_display = ('title', 'priority',  'is_ready')        
    inlines = [
        CommentInline,    
    ]

    def view_is_ready(self, obj):
        return obj.is_ready

admin.site.register(models.Todo_post, Todo_postAdmin)
admin.site.register(models.Comment)
