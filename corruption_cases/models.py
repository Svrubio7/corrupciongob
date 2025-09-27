from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils import timezone
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
    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="Slug")
    short_description = models.TextField(max_length=500, verbose_name="Descripción corta")
    full_description = models.TextField(verbose_name="Descripción completa")
    
    # Key details
    date = models.DateField(verbose_name="Fecha")
    amount = models.DecimalField(
        max_digits=20, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        help_text="Importe en euros",
        verbose_name="Importe"
    )
    main_image = models.ImageField(
        upload_to='cases/', 
        blank=True, 
        null=True,
        help_text="Tamaño máximo: 10MB",
        verbose_name="Imagen principal"
    )
    
    # Relationships
    political_party = models.ForeignKey(
        PoliticalParty, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Partido político"
    )
    institution = models.ForeignKey(
        Institution, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Institución"
    )
    corruption_type = models.ForeignKey(
        CorruptionType, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Tipo de corrupción"
    )
    region = models.ForeignKey(
        Region, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Región"
    )
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Etiquetas")
    
    # Publication type
    publication_type = models.CharField(
        max_length=50,
        choices=[
            ('article', 'Artículo'),
            ('case', 'Caso'),
            ('opinion', 'Artículo de Opinión'),
            ('report', 'Informe'),
            ('investigation', 'Investigación'),
            ('news', 'Noticia'),
            ('video', 'Vídeo'),
            ('other', 'Otro'),
        ],
        default='article',
        help_text="Tipo de publicación",
        verbose_name="Tipo de publicación"
    )
    
    # Author name
    author_name = models.CharField(
        max_length=200,
        blank=True,
        help_text="Nombre del autor del artículo",
        verbose_name="Nombre del autor"
    )
    
    # External URL (for any publication type that should redirect to external link)
    external_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL externa para redirigir (para videos, artículos, noticias, etc.)",
        verbose_name="URL externa"
    )
    
    # Annual amount fields
    is_annual_amount = models.BooleanField(
        default=False,
        help_text="¿Es esta cantidad un gasto anual?",
        verbose_name="Es importe anual"
    )
    start_date = models.DateField(
        null=True,
        blank=True,
        help_text="Fecha de comienzo del gasto (para calcular años de duración)",
        verbose_name="Fecha de inicio"
    )
    
    # Metadata
    sources = models.TextField(help_text="Enlaces a fuentes, separados por líneas nuevas", verbose_name="Fuentes")
    is_featured = models.BooleanField(default=False, verbose_name="Es destacado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    class Meta:
        ordering = ['-amount', '-date', '-created_at']  # Order by amount by default
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
    
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
    
    def get_total_amount(self):
        """Calculate total amount considering annual payments"""
        if self.is_annual_amount and self.start_date:
            from datetime import date
            today = date.today()
            years = today.year - self.start_date.year
            # Add 1 year if we're past the anniversary date
            if today.month > self.start_date.month or (today.month == self.start_date.month and today.day >= self.start_date.day):
                years += 1
            return self.amount * max(1, years)  # At least 1 year
        return self.amount
    
    def get_years_duration(self):
        """Get number of years this payment has been ongoing"""
        if self.is_annual_amount and self.start_date:
            from datetime import date
            today = date.today()
            years = today.year - self.start_date.year
            # Add 1 year if we're past the anniversary date
            if today.month > self.start_date.month or (today.month == self.start_date.month and today.day >= self.start_date.day):
                years += 1
            return max(1, years)
        return 1
    
    def get_processed_description(self):
        """Process description to embed images in text and handle titles/subtitles"""
        import re
        from django.utils.safestring import mark_safe
        
        description = self.full_description
        images = list(self.case_images.all().order_by('order', 'created_at'))
        
        # First, process image markers
        pattern = r'<imagen(\d+)>'
        matches = re.findall(pattern, description)
        
        for match in matches:
            image_index = int(match) - 1  # Convert to 0-based index
            marker = f'<imagen{match}>'
            
            if 0 <= image_index < len(images):
                image = images[image_index]
                # Create HTML for the embedded image
                image_html = f'''
                <div class="embedded-image my-6">
                    <img src="{image.image.url}" alt="{image.caption or 'Imagen'}" 
                         class="w-full h-auto rounded-lg shadow-md">
                    {f'<p class="text-sm text-gray-600 mt-2 text-center italic">{image.caption}</p>' if image.caption else ''}
                </div>
                '''
                description = description.replace(marker, image_html)
            else:
                # Remove marker if image doesn't exist
                description = description.replace(marker, '')
        
        # Process titles and subtitles
        # Handle ## subtitles first (to avoid conflicts with # titles)
        description = re.sub(r'^##(.+?)$', r'<h3 class="text-xl font-bold text-palette-black mt-6 mb-3">\1</h3>', description, flags=re.MULTILINE)
        # Handle # titles
        description = re.sub(r'^#(.+?)$', r'<h2 class="text-2xl font-bold text-palette-black mt-8 mb-4">\1</h2>', description, flags=re.MULTILINE)
        
        # Convert line breaks to paragraphs
        # Split by double line breaks first
        paragraphs = description.split('\n\n')
        processed_paragraphs = []
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if paragraph:
                # If it's not already HTML (contains tags), wrap in <p>
                if not re.search(r'<[^>]+>', paragraph):
                    # Replace single line breaks within paragraphs with <br> tags
                    paragraph = paragraph.replace('\n', '<br>')
                    paragraph = f'<p class="mb-4 leading-relaxed">{paragraph}</p>'
                processed_paragraphs.append(paragraph)
        
        # Join paragraphs with proper HTML spacing (no extra newlines)
        final_description = ''.join(processed_paragraphs)
        
        return mark_safe(final_description)
    
    def clean(self):
        """Validate file size"""
        super().clean()
        if self.main_image:
            # Check file size (10MB limit)
            if self.main_image.size > 10 * 1024 * 1024:  # 10MB in bytes
                raise ValidationError({
                    'main_image': 'El tamaño del archivo debe ser menor a 10MB. Por favor comprime la imagen o elige un archivo más pequeño.'
                })

class CaseImage(models.Model):
    case = models.ForeignKey(CorruptionCase, on_delete=models.CASCADE, related_name='case_images', verbose_name="Publicación")
    image = models.ImageField(
        upload_to='cases/detail/',
        help_text="Tamaño máximo: 10MB",
        verbose_name="Imagen"
    )
    caption = models.CharField(max_length=200, blank=True, verbose_name="Título")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Imagen de publicación"
        verbose_name_plural = "Imágenes de publicación"
    
    def __str__(self):
        return f"{self.case.title} - {self.caption or 'Imagen'}"
    
    def clean(self):
        """Validate file size"""
        super().clean()
        if self.image:
            # Check file size (10MB limit)
            if self.image.size > 10 * 1024 * 1024:  # 10MB in bytes
                raise ValidationError({
                    'image': 'El tamaño del archivo debe ser menor a 10MB. Por favor comprime la imagen o elige un archivo más pequeño.'
                })
