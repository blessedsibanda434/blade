from django.db import models
from django.shortcuts import reverse


class Video(models.Model):
    STATUS = (
        ('Draft', 'Draft'),
        ('Publish', 'Published')
    )
    title = models.CharField(max_length=120)
    url = models.URLField()
    status = models.CharField(choices=STATUS, max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('videos:video_detail', args=[self.slug,])

    
