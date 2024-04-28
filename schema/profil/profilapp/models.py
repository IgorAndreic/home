from django.db import models
from django.core.files.storage import FileSystemStorage
from django.forms import ValidationError


class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = "Folder"
        verbose_name_plural = "Folders"

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=255)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='uploads/')

    def save(self, *args, **kwargs):
        if self.folder is None:
            raise ValidationError("Необходимо указать папку перед сохранением файла.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
