from django.db import models
from .val import ContentTypeRestrictedFileField

class Document(models.Model):
    document = ContentTypeRestrictedFileField(
		  upload_to='./documents/',
		  content_types=['text/plain','application/vnd.openxmlformats-officedocument.wordprocessingml.document','application/msword'], 
		  max_upload_size=5242880
		  )
    uploaded_at = models.DateTimeField(auto_now_add=True)

