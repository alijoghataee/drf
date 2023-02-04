from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=150)
    story_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='book_image/', blank=True, null=True)
    fav = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
