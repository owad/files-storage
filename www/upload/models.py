from django.db import models
from datetime import datetime
from www.settings import USER_UPLOADS

class File(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="%s/%s/%s" % (USER_UPLOADS, 'owad', datetime.now().strftime('%Y/%m/')))
    content_type = models.CharField(max_length=32)
    date_add = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

