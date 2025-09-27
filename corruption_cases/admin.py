from django.contrib import admin
from django.utils.html import format_html
from .models import (
    PoliticalParty, Institution, CorruptionType, Region, 
    Tag, CorruptionCase, ImagenPublicacion
)

@admin.register(PoliticalParty)
class PoliticalPartyAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'color_display', 'created_at']
    search_fields = ['name', 'short_name']
    list_filter = ['created_at']
    def color_display(self, obj):
        return format_html(
            '<div style="background-color: {}; width: 20px; height: 20px; border-radius: 3px;"></div>',
            obj.color
        )
    color_display.short_description = 'Color'

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'institution_type', 'region', 'created_at']
    list_filter = ['institution_type', 'region', 'created_at']
    search_fields = ['name', 'region']

@admin.register(CorruptionType)
class CorruptionTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'autonomous_community', 'created_at']
    list_filter = ['autonomous_community', 'created_at']
    search_fields = ['name', 'autonomous_community']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

class ImagenPublicacionInline(admin.TabularInline):
    model = ImagenPublicacion
    extra = 1
    fields = ['imagen', 'titulo', 'orden']

@admin.register(CorruptionCase)
class CorruptionCaseAdmin(admin.ModelAdmin):
    list_display = [
        'titulo', 'fecha', 'amount_display', 'partido_politico', 
        'institucion', 'tipo_publicacion', 'nombre_autor', 'es_destacado', 'fecha_creacion'
    ]
    list_filter = [
        'fecha', 'partido_politico', 'institucion', 'tipo_corrupcion', 
        'region', 'tipo_publicacion', 'es_importe_anual', 'es_destacado', 'fecha_creacion'
    ]
    search_fields = ['titulo', 'descripcion_corta', 'descripcion_completa', 'nombre_autor']
    prepopulated_fields = {'slug': ('titulo',)}
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    inlines = [ImagenPublicacionInline]
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'slug', 'descripcion_corta', 'descripcion_completa')
        }),
        ('Detalles de Publicación', {
            'fields': ('tipo_publicacion', 'nombre_autor', 'url_externa')
        }),
        ('Detalles Clave', {
            'fields': ('fecha', 'importe', 'imagen_principal')
        }),
        ('Detalles de Importe Anual', {
            'fields': ('es_importe_anual', 'fecha_inicio'),
            'description': 'Marca si este es un pago anual y establece la fecha de inicio'
        }),
        ('Categorización', {
            'fields': ('partido_politico', 'institucion', 'tipo_corrupcion', 'region', 'etiquetas')
        }),
        ('Contenido', {
            'fields': ('fuentes', 'es_destacado')
        }),
        ('Metadatos', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    def amount_display(self, obj):
        return obj.get_amount_display()
    amount_display.short_description = 'Amount'
    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'partido_politico', 'institucion', 'tipo_corrupcion', 'region'
        )

# Customize admin site
admin.site.site_header = "Corruption Portal Admin"
admin.site.site_title = "Corruption Portal"
admin.site.index_title = "Welcome to Corruption Portal Administration"
