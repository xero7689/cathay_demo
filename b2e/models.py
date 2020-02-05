from django.db import models

class SubmittedURL(models.Model):
    url = models.URLField(unique=True)
    host = models.CharField(db_index=True, max_length=255)
    submit_num = models.IntegerField(default=0)
    click_num = models.IntegerField(default=0)

