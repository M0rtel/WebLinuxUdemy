from django.db import models

# Create your models here.
class PostBlog(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='img/')

    def continue_post(self):
        return self.text[:100]

    def __str__(self):
        return self.title