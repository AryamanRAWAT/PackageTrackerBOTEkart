from django.db import models
from datetime import datetime

# Create your models here.
# tracking id, chat id, is_active, date_created
#one class = one table

class UserInfo(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    tracking_id = models.CharField(max_length=255)
    chat_id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=datetime.now())

    # def __str__(self):
    #     return self.chat_id
    
    class Meta:
        unique_together = ('tracking_id', 'chat_id',)