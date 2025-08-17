from django.contrib import admin
from django.utils.html import format_html
from .models import (
    PoliticalParty, Institution, CorruptionType, Region, 
    Tag, CorruptionCase, CaseImage
)

@admin.register(PoliticalParty)
class PoliticalPartyAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'color_display', 'created_at']
    search_fields = ['name', 'short_name']
    list_filter = ['created_at']
    list_per_page = None
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
    list_per_page = None

@admin.register(CorruptionType)
class CorruptionTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']
    list_per_page = None

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'autonomous_community', 'created_at']
    list_filter = ['autonomous_community', 'region', 'created_at']
    search_fields = ['name', 'autonomous_community']
    list_per_page = None

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_per_page = None

class CaseImageInline(admin.TabularInline):
    model = CaseImage
    extra = 1
    fields = ['image', 'caption', 'order']
    list_per_page = None

@admin.register(CorruptionCase)
class CorruptionCaseAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'date', 'amount_display', 'political_party', 
        'institution', 'is_featured', 'created_at'
    ]
    list_filter = [
        'date', 'political_party', 'institution', 'corruption_type', 
        'region', 'is_featured', 'created_at'
    ]
    search_fields = ['title', 'short_description', 'full_description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [CaseImageInline]
    list_per_page = None
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_description', 'full_description')
        }),
        ('Key Details', {
            'fields': ('date', 'amount', 'main_image')
        }),
        ('Categorization', {
            'fields': ('political_party', 'institution', 'corruption_type', 'region', 'tags')
        }),
        ('Content', {
            'fields': ('sources', 'is_featured')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    def amount_display(self, obj):
        return obj.get_amount_display()
    amount_display.short_description = 'Amount'
    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'political_party', 'institution', 'corruption_type', 'region'
        )

# Customize admin site
admin.site.site_header = "Corruption Portal Admin"
admin.site.site_title = "Corruption Portal"
admin.site.index_title = "Welcome to Corruption Portal Administration"
