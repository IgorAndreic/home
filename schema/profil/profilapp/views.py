from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Folder, File
from .serializers import FolderSerializer, FileSerializer
from django.http import FileResponse, HttpResponse
import mimetypes

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        parent_id = self.request.query_params.get('parent_id')

        if parent_id is not None:
            if parent_id.lower() == 'null':
                queryset = queryset.filter(parent__isnull=True)
            else:
                try:
                    parent_id = int(parent_id)
                    queryset = queryset.filter(parent__id=parent_id)
                except ValueError:
                    # Обработка случая, когда parent_id не может быть преобразован в int
                    queryset = queryset.none()
        return queryset

    def perform_create(self, serializer):
        serializer.save()

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        print(self.request.data)
        folder_id = self.request.data.get('folder')
        print(folder_id)
        folder = get_object_or_404(Folder, id=folder_id)  # Используем get_object_or_404
        print(folder)
        serializer.save(folder=folder)
