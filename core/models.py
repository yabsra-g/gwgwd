from django.db import models

class Artwork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    place = models.CharField(max_length=200, blank=True, null=True)
    # Link to Country (replacing category)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, blank=True, related_name='artworks')
    # Link to Artist
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True, blank=True, related_name='artworks')
    image = models.ImageField(upload_to='artworks/images/', blank=True, null=True)
    video = models.FileField(upload_to='artworks/videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='artists/', blank=True, null=True)
    description = models.TextField() # Renamed from overview
    website = models.URLField(blank=True, null=True)
    ROLE_CHOICES = [
        ('Team Leader', 'Project Leader'),
        ('Artist', 'Artist'),
        ('Other', 'Other'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Artist')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='activities/images/', blank=True, null=True)
    video = models.FileField(upload_to='activities/videos/', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Activities"
        ordering = ['-date']

    def __str__(self):
        return self.title


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Must match the category name in Artwork (e.g., 'Morocco', 'Brazil')")
    description = models.TextField()
    image = models.ImageField(upload_to='countries/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']

    def __str__(self):
        return self.name
