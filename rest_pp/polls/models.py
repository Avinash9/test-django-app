from django.db import models

# Create your models here.


class LogUser(models.Model):
    id = models.CharField(max_length=16,primary_key=True)


class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=300)
    time_stamp = models.DateTimeField()
    is_sent = models.BooleanField()
    logs = models.ForeignKey(LogUser)









