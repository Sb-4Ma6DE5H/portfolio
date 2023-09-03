from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    content_1 = models.TextField()
    content_2 = models.TextField()
    content_3 = models.TextField()
    content_4 = models.TextField()
    content_5 = models.TextField()
    featur_1 = models.CharField(max_length=100)
    featur_2 = models.CharField(max_length=100)
    featur_3 = models.CharField(max_length=100)
    project_url = models.CharField(max_length=500)

    is_websites = models.BooleanField(default=False)
    is_web_apps = models.BooleanField(default=False)
    is_ecommerce = models.BooleanField(default=False)
    is_updates = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class CheckUpImage(models.Model):
    image = models.ImageField(upload_to = 'images/')
