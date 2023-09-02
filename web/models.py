from django.db import models

# Create your models here.
from django.db import models

class PortfolioItem(models.Model):
    image = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')  # Add an image field
    # Add other fields as needed, such as image, date, etc.

    def __str__(self):
        return self.title