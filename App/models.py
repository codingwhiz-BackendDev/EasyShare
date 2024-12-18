from django.db import models
from datetime import datetime
import uuid
# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to='Files', max_length=255, null=True)
    fileName = models.CharField(max_length=255,null=True)
    uniqueLink = models.UUIDField(default=uuid.uuid4, unique=True,null=True)
    timeUploaded = models.DateTimeField(default=datetime.now,null=True) 
    fileSize = models.CharField(max_length=255,null=True)
    fileType = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return str(self.fileName)
    