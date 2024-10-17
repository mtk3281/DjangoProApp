from django.db import models
import uuid
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


class BlogPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='covers/')
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique_for_date='created_at')

    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
        models.Index(fields=['-title']),
        ]
    
    def get_absolute_url(self):
        if self.created_at and self.slug:
            return reverse('blog_post_detail', args=[self.created_at.year, self.created_at.month, self.created_at.day, self.slug])
        return "#"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class BlogImage(models.Model):
    post = models.ForeignKey(BlogPost, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="covers/")
    alt_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.alt_text


class Comment(models.Model):
    post = models.ForeignKey(BlogPost,
                    on_delete=models.CASCADE,
                    related_name='comments'
                    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'