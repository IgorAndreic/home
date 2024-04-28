from rest_framework import serializers
from .models import Folder, File

class FolderSerializer(serializers.ModelSerializer):
    children = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Folder
        fields = ['id', 'name', 'parent', 'is_root','children']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'folder']
