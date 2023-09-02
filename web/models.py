from django.db import models

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)  # Assuming you have a title field
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')  # Add an image field
    # Add other fields as needed, such as date, etc.

    def __str__(self):
        return self.title
