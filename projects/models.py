from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from markdownx.models import MarkdownxField


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    external_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    
    class Meta:
        ordering = ['order', '-created_date']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = MarkdownxField()
    summary = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='blog/', blank=True)
    author = models.CharField(max_length=100, default='Admin')
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-published_date']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.summary and self.content:
            text_content = str(self.content)
            self.summary = text_content[:297] + '...' if len(text_content) > 300 else text_content
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('discord', 'Discord'),
        ('stackoverflow', 'Stack Overflow'),
        ('dribbble', 'Dribbble'),
        ('behance', 'Behance'),
        ('medium', 'Medium'),
        ('dev', 'Dev.to'),
        ('telegram', 'Telegram'),
        ('whatsapp', 'WhatsApp'),
    ]
    
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, unique=True)
    name = models.CharField(max_length=100)
    url = models.URLField()
    icon_class = models.CharField(max_length=100, default='fab fa-link', help_text="Font Awesome icon class")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('database', 'Database'),
        ('devops', 'DevOps'),
        ('tools', 'Tools'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    icon_class = models.CharField(max_length=100, blank=True, help_text="Font Awesome icon class")
    proficiency = models.IntegerField(default=80, help_text="Proficiency percentage (1-100)")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
    
    def __str__(self):
        return f"{self.title} at {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Profile(models.Model):
    """Single model to store all personal information"""
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
    
    name = models.CharField(max_length=200, default='Your Name')
    title = models.CharField(max_length=200, default='Full Stack Developer')
    subtitle = models.CharField(max_length=500, blank=True, help_text="Short tagline under your title")
    
    profile_image = models.ImageField(upload_to='profile/', blank=True, help_text="Your photo")
    
    email = models.EmailField(default='your.email@example.com')
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    
    about_title = models.CharField(max_length=200, blank=True)
    about_subtitle = models.CharField(max_length=500, blank=True)
    about_content = models.TextField(blank=True, help_text="Main about section content")
    about_image = models.ImageField(upload_to='profile/', blank=True)
    
    resume_cv = models.FileField(upload_to='profile/', blank=True, help_text="Upload your CV/Resume PDF")
    
    hero_stats = models.JSONField(default=dict, blank=True, help_text='{"projects": "50+", "years": "3+", "clients": "30+"}')
    
    response_time = models.CharField(max_length=100, blank=True, default='Within 24 hours')
    
    footer_text = models.TextField(blank=True, help_text="Custom footer text")
    footer_copyright = models.CharField(max_length=200, blank=True)
    
    seo_title = models.CharField(max_length=200, blank=True)
    seo_description = models.TextField(blank=True)
    seo_keywords = models.CharField(max_length=500, blank=True)
    
    google_analytics_id = models.CharField(max_length=50, blank=True, help_text="GA4 Measurement ID")
    
    updated_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            Profile.objects.all().delete()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, default='fas fa-code', help_text="Font Awesome icon class")
    icon_color = models.CharField(max_length=50, default='sky', help_text="Tailwind color class (sky, emerald, purple, orange, teal, pink)")
    features = models.JSONField(default=list, blank=True, help_text='["Feature 1", "Feature 2"]')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return self.title
