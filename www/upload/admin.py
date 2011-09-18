from django.contrib import admin
from upload.models import File

class FileAdmin(admin.ModelAdmin):
    model = File
    list_display = ('title', 'file')
    
admin.site.register(File, FileAdmin)
