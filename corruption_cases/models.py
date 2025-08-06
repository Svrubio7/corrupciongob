from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.core.exceptions import ValidationError
import os

class PoliticalParty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=20, blank=True)
    logo = models.ImageField(upload_to='parties/', blank=True, null=True)
    color = models.CharField(max_length=7, default='#000000')  # Hex color
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Political Parties"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Institution(models.Model):
    INSTITUTION_TYPES = [
        ('central', 'Gobierno Central'),
        ('autonomous', 'Comunidad Autónoma'),
        ('provincial', 'Diputación Provincial'),
        ('municipal', 'Ayuntamiento'),
        ('other', 'Otro'),
    ]
    
    name = models.CharField(max_length=200)
    institution_type = models.CharField(max_length=20, choices=INSTITUTION_TYPES)
    region = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.get_institution_type_display()})"

class CorruptionType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    autonomous_community = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class CorruptionCase(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    short_description = models.TextField(max_length=500)
    full_description = models.TextField()
    
    # Key details
    date = models.DateField()
    amount = models.DecimalField(
        max_digits=20, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        help_text="Amount in euros"
    )
    main_image = models.ImageField(
        upload_to='cases/', 
        blank=True, 
        null=True,
        help_text="Maximum file size: 10MB"
    )
    
    # Relationships
    political_party = models.ForeignKey(
        PoliticalParty, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    institution = models.ForeignKey(
        Institution, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    corruption_type = models.ForeignKey(
        CorruptionType, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    region = models.ForeignKey(
        Region, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    tags = models.ManyToManyField(Tag, blank=True)
    
    # Metadata
    sources = models.TextField(help_text="Links to sources, separated by new lines")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-amount', '-date', '-created_at']  # Order by amount by default
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
            # Ensure uniqueness
            original_slug = self.slug
            for x in range(1, 1000):
                if not CorruptionCase.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                    break
                self.slug = f"{original_slug}-{x}"
        super().save(*args, **kwargs)
    
    def get_amount_display(self):
        """Format amount as currency"""
        return f"€{self.amount:,.2f}"
    
    def clean(self):
        """Validate file size"""
        super().clean()
        if self.main_image:
            # Check file size (10MB limit)
            if self.main_image.size > 10 * 1024 * 1024:  # 10MB in bytes
                raise ValidationError({
                    'main_image': 'File size must be under 10MB. Please compress the image or choose a smaller file.'
                })

class CaseImage(models.Model):
    case = models.ForeignKey(CorruptionCase, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(
        upload_to='cases/detail/',
        help_text="Maximum file size: 10MB"
    )
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
    
    def __str__(self):
        return f"{self.case.title} - {self.caption or 'Image'}"
    
    def clean(self):
        """Validate file size"""
        super().clean()
        if self.image:
            # Check file size (10MB limit)
            if self.image.size > 10 * 1024 * 1024:  # 10MB in bytes
                raise ValidationError({
                    'image': 'File size must be under 10MB. Please compress the image or choose a smaller file.'
                })
