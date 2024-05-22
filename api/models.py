from django.db import models


class New(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return self.title
