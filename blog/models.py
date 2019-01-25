from django.utils import timezone

from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField



class PublishedPostsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='Published')


class Post(models.Model):
    STATUS = (
        ('Draft', 'D'),
        ('Published', 'P')
    )
    title = models.CharField(max_length=150)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image_header = models.ImageField(upload_to='images/image_headers', null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=9)
    slug = models.SlugField()
    pub_date = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    published = PublishedPostsManager()

    class Meta:
        ordering = ('-pub_date','-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.created.year,
                             self.created.strftime('%m'),
                             self.created.strftime('%d'),
                             self.slug])

    def save(self, *args, **kwargs):
        if self.status == 'Published':
            if not self.pub_date:
                self.pub_date = timezone.now()
        else: 
            self.pub_date = None
        super(Post, self).save(*args, **kwargs)
    


