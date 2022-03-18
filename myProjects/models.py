from django.db import models

class Event(models.Model):
    event_image = models.ImageField(upload_to='img/')
    event_text = models.CharField(max_length=300)

    def __str__(self):
        return self.event_text[:10]
