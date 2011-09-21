from django.db import models
from datetime import datetime
from case.models import Case
from settings import USER_UPLOADS

class File(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="%s/%s/%s" % (USER_UPLOADS, 'owad', datetime.now().strftime('%Y/%m/')))
    content_type = models.CharField(max_length=32)
    date_add = models.DateTimeField(auto_now_add=True)
    
    case = models.ForeignKey(Case, verbose_name='sprawa')

    def __unicode__(self):
        return self.title

