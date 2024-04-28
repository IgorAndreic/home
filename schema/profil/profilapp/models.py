from django.db import models

class Folder(models.Model):
    name = models.CharField(max_length=255, null=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_root = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.parent is None:
            self.is_root = True
        else:
            self.is_root = False
        super().save(*args, **kwargs)  

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=255, null=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return self.name
