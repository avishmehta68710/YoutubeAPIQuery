from django.db import models

# Create your models here.


class Video(models.Model):
    index = models.AutoField(primary_key=True)
    video_title = models.TextField()
    description = models.TextField()
    publishing_date_time = models.DateTimeField()
    thumbnails_urls = models.TextField()
    channel_id = models.TextField()
    video_id = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.video_title


class APIKey(models.Model):
    key = models.TextField()
    is_limit_over = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'APIKey'
        verbose_name_plural = 'APIKeys'

    def __str__(self):
        return self.key
