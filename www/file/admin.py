from django.contrib import admin
from file.models import File

class FileAdmin(admin.ModelAdmin):
    model = File
    
admin.site.register(File, FileAdmin)
