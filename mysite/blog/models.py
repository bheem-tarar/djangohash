from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField


STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)
    timestamp=models.DateTimeField(auto_now_add=True, editable=False)
    utimestamp=models.DateTimeField(auto_now=True, editable=False)
    track=models.TextField()
    utrack=models.TextField()
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='Inactive')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, max_length=255)
    timestamp=models.DateTimeField(auto_now_add=True, editable=False)
    utimestamp=models.DateTimeField(auto_now=True, editable=False)
    track=models.TextField()
    utrack=models.TextField()
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='Inactive')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    slug = models.SlugField(unique=True, max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_author')
    thumbnail = models.ImageField(upload_to='post_thumbnails/',)
    feature_image = models.ImageField(upload_to='post_feature_images/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(default=timezone.now)
    timestamp=models.DateTimeField(auto_now_add=True, editable=False)
    utimestamp=models.DateTimeField(auto_now=True, editable=False)
    track=models.TextField()
    utrack=models.TextField()
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='Inactive')
   
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts_category'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='post_tag',
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)
    timestamp=models.DateTimeField(auto_now_add=True, editable=False)
    utimestamp=models.DateTimeField(auto_now=True, editable=False)
    track=models.TextField()
    utrack=models.TextField()
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    utimestamp = models.DateTimeField(auto_now=True, editable=False)
    track = models.TextField()
    utrack = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return f"{self.name} - {self.subject}"