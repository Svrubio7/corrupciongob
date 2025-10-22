from django.contrib import admin
from django.utils.html import format_html
from .models import (
    PoliticalParty, Institution, CorruptionType, Region, 
    Tag, Country, CorruptionCase, CaseImage
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

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'created_at']
    search_fields = ['name', 'code']
    list_filter = ['created_at']

class CaseImageInline(admin.TabularInline):
    model = CaseImage
    extra = 1
    fields = ['image', 'caption', 'order']

@admin.register(CorruptionCase)
class CorruptionCaseAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'date', 'publication_date', 'amount_display', 'political_party', 
        'institution', 'publication_type', 'author_name', 'is_featured', 'created_at'
    ]
    list_filter = [
        'date', 'publication_date', 'political_party', 'institution', 'corruption_type', 
        'region', 'country', 'publication_type', 'is_annual_amount', 'is_featured', 'created_at'
    ]
    search_fields = ['title', 'short_description', 'full_description', 'author_name', 'country__name']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [CaseImageInline]
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'slug', 'short_description', 'full_description')
        }),
        ('Detalles de Publicación', {
            'fields': ('publication_type', 'author_name', 'external_url', 'publication_date')
        }),
        ('Detalles Clave', {
            'fields': ('date', 'amount', 'main_image')
        }),
        ('Detalles de Importe Anual', {
            'fields': ('is_annual_amount', 'start_date'),
            'description': 'Marca si este es un pago anual y establece la fecha de inicio'
        }),
        ('Categorización', {
            'fields': ('political_party', 'institution', 'corruption_type', 'region', 'country', 'tags')
        }),
        ('Contenido', {
            'fields': ('sources', 'is_featured')
        }),
        ('Metadatos', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    def amount_display(self, obj):
        return obj.get_amount_display()
    amount_display.short_description = 'Amount'
    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'political_party', 'institution', 'corruption_type', 'region', 'country'
        )

# Customize admin site
admin.site.site_header = "Corruption Portal Admin"
admin.site.site_title = "Corruption Portal"
admin.site.index_title = "Welcome to Corruption Portal Administration"
