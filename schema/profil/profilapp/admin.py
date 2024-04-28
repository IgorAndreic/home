from django.contrib import admin
from .models import Folder, File

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['name', 'folder']
