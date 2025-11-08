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

class Country(models.Model):
    """Country model for tracking international money destinations"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre del país")
    code = models.CharField(max_length=3, unique=True, verbose_name="Código ISO", help_text="Código ISO 3166-1 alpha-3")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = "País"
        verbose_name_plural = "Países"
    
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
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Importe en euros (obligatorio solo para casos)",
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
    country = models.ForeignKey(
        'Country',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="País destino",
        help_text="País al que se destina el dinero público"
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
    publication_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Fecha de publicación del contenido",
        verbose_name="Fecha de publicación"
    )
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
        if self.amount is None:
            return "Sin importe"
        return f"€{self.amount:,.2f}"
    
    def get_total_amount(self):
        """Calculate total amount considering annual payments"""
        if self.amount is None:
            return 0
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
                caption_html = f'<p class="image-caption">{image.caption}</p>' if image.caption else ''
                image_html = f'<div class="embedded-image"><img src="{image.image.url}" alt="{image.caption or "Imagen"}">{caption_html}</div>'
                description = description.replace(marker, image_html)
            else:
                # Remove marker if image doesn't exist
                description = description.replace(marker, '')
        
        # Process titles and subtitles
        # Handle ## subtitles first (to avoid conflicts with # titles) - no special spacing
        description = re.sub(r'^##\s*(.+?)$', r'<h3 class="text-xl font-bold text-palette-black">\1</h3>', description, flags=re.MULTILINE)
        # Handle # titles - no special spacing
        description = re.sub(r'^#\s*(.+?)$', r'<h2 class="text-2xl font-bold text-palette-black">\1</h2>', description, flags=re.MULTILINE)
        
        # Process line breaks - preserve exact number of line breaks
        # First, handle HTML tags (titles/subtitles) by splitting around them
        parts = re.split(r'(<h[23][^>]*>.*?</h[23]>)', description, flags=re.DOTALL)
        processed_parts = []
        
        for part in parts:
            if re.match(r'<h[23]', part):
                # This is an HTML tag, keep as is
                processed_parts.append(part)
            else:
                # Process text content
                processed_parts.append(self._process_text_content(part))
        
        # Join all parts
        final_description = ''.join(processed_parts)
        
        return mark_safe(final_description)
    
    def _process_text_content(self, text):
        """Process text content to preserve exact number of empty lines and handle bullet points"""
        if not text.strip():
            return ''
        
        # Process each line individually to detect bullet points and preserve empty lines
        lines = text.split('\n')
        processed_lines = []
        current_list_items = []
        
        for line in lines:
            if line.strip() == '':
                # Empty line - preserve it as <br>
                if current_list_items:
                    list_html = '<ul class="list-disc list-inside space-y-0">'
                    for item in current_list_items:
                        list_html += f'<li class="leading-relaxed">{item}</li>'
                    list_html += '</ul>'
                    processed_lines.append(list_html)
                    current_list_items = []
                processed_lines.append('<br>')
            elif line.startswith('-'):
                # It's a bullet point
                item_text = line[1:].strip()
                current_list_items.append(item_text)
            else:
                # Regular text - close any pending list first
                if current_list_items:
                    list_html = '<ul class="list-disc list-inside space-y-0">'
                    for item in current_list_items:
                        list_html += f'<li class="leading-relaxed">{item}</li>'
                    list_html += '</ul>'
                    processed_lines.append(list_html)
                    current_list_items = []
                processed_lines.append(line.strip())
        
        # Close any remaining list
        if current_list_items:
            list_html = '<ul class="list-disc list-inside space-y-0">'
            for item in current_list_items:
                list_html += f'<li class="leading-relaxed">{item}</li>'
            list_html += '</ul>'
            processed_lines.append(list_html)
        
        # Join all processed elements - add <br> between text lines, empty lines are already <br>
        if processed_lines:
            # Add <br> between consecutive text elements (not after <br> or <ul>)
            final_content = []
            for i, element in enumerate(processed_lines):
                final_content.append(element)
                # Add <br> between text elements if next element is also text
                if (i < len(processed_lines) - 1 and 
                    not element.endswith('<br>') and 
                    not element.startswith('<ul') and
                    not processed_lines[i + 1].startswith('<ul')):
                    final_content.append('<br>')
            
            paragraph_content = ''.join(final_content)
            paragraph_html = f'<p class="leading-relaxed">{paragraph_content}</p>'
            return paragraph_html
        
        return ''
    
    def clean(self):
        """Validate file size and required fields based on publication type"""
        super().clean()
        
        # Validate amount is required for cases
        if self.publication_type == 'case' and (self.amount is None or self.amount == 0):
            raise ValidationError({
                'amount': 'El importe es obligatorio para publicaciones de tipo "Caso".'
            })
        
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
