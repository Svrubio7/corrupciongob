from rest_framework import serializers
from .models import (
    PoliticalParty, Institution, CorruptionType, Region, 
    Tag, Country, CorruptionCase, CaseImage
)

class PoliticalPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticalParty
        fields = ['id', 'name', 'short_name', 'logo', 'color', 'created_at']

class InstitutionSerializer(serializers.ModelSerializer):
    institution_type_display = serializers.CharField(source='get_institution_type_display', read_only=True)
    
    class Meta:
        model = Institution
        fields = ['id', 'name', 'institution_type', 'institution_type_display', 'region', 'created_at']

class CorruptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorruptionType
        fields = ['id', 'name', 'description', 'created_at']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'autonomous_community', 'created_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'code', 'created_at']

class CaseImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    def get_image(self, obj):
        """Return HTTPS URL for image"""
        if obj.image:
            request = self.context.get('request')
            if request:
                url = request.build_absolute_uri(obj.image.url)
                # Force HTTPS
                return url.replace('http://', 'https://')
            return obj.image.url.replace('http://', 'https://')
        return None
    
    class Meta:
        model = CaseImage
        fields = ['id', 'image', 'caption', 'order', 'created_at']

class CorruptionCaseListSerializer(serializers.ModelSerializer):
    """Serializer for list view - includes basic info"""
    political_party = PoliticalPartySerializer(read_only=True)
    institution = InstitutionSerializer(read_only=True)
    corruption_type = CorruptionTypeSerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    amount_display = serializers.CharField(source='get_amount_display', read_only=True)
    total_amount = serializers.DecimalField(source='get_total_amount', max_digits=20, decimal_places=2, read_only=True)
    years_duration = serializers.IntegerField(source='get_years_duration', read_only=True)
    publication_type_display = serializers.SerializerMethodField(read_only=True)
    main_image = serializers.SerializerMethodField()
    
    def get_main_image(self, obj):
        """Return HTTPS URL for main image"""
        if obj.main_image:
            request = self.context.get('request')
            if request:
                url = request.build_absolute_uri(obj.main_image.url)
                # Force HTTPS
                return url.replace('http://', 'https://')
            return obj.main_image.url.replace('http://', 'https://')
        return None
    
    def get_publication_type_display(self, obj):
        """Get the display value for publication_type field"""
        if hasattr(obj, 'get_publication_type_display'):
            return obj.get_publication_type_display()
        # Fallback for cases where the method doesn't exist yet
        publication_type_choices = {
            'article': 'Artículo',
            'case': 'Caso',
            'opinion': 'Artículo de Opinión',
            'report': 'Informe',
            'investigation': 'Investigación',
            'news': 'Noticia',
            'video': 'Vídeo',
            'other': 'Otro',
        }
        return publication_type_choices.get(obj.publication_type, obj.publication_type or 'Artículo')
    
    class Meta:
        model = CorruptionCase
        fields = [
            'id', 'title', 'slug', 'short_description', 'date', 'amount', 
            'amount_display', 'total_amount', 'years_duration', 'main_image', 
            'political_party', 'institution', 'corruption_type', 'region', 'country', 'tags', 
            'publication_type', 'publication_type_display', 'author_name', 
            'external_url', 'is_annual_amount', 'start_date', 'is_featured', 'created_at'
        ]

class CorruptionCaseDetailSerializer(serializers.ModelSerializer):
    """Serializer for detail view - includes all info"""
    political_party = PoliticalPartySerializer(read_only=True)
    institution = InstitutionSerializer(read_only=True)
    corruption_type = CorruptionTypeSerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    case_images = CaseImageSerializer(many=True, read_only=True)
    amount_display = serializers.CharField(source='get_amount_display', read_only=True)
    total_amount = serializers.DecimalField(source='get_total_amount', max_digits=20, decimal_places=2, read_only=True)
    years_duration = serializers.IntegerField(source='get_years_duration', read_only=True)
    publication_type_display = serializers.SerializerMethodField(read_only=True)
    processed_description = serializers.SerializerMethodField()
    main_image = serializers.SerializerMethodField()
    
    def get_main_image(self, obj):
        """Return HTTPS URL for main image"""
        if obj.main_image:
            request = self.context.get('request')
            if request:
                url = request.build_absolute_uri(obj.main_image.url)
                # Force HTTPS
                return url.replace('http://', 'https://')
            return obj.main_image.url.replace('http://', 'https://')
        return None
    
    def get_processed_description(self, obj):
        """Return processed description with HTTPS URLs"""
        description = obj.get_processed_description()
        # Force HTTPS in any URLs within the description
        if description:
            description = description.replace('http://www.degu.es/', 'https://www.degu.es/')
            description = description.replace('http://degu.es/', 'https://degu.es/')
        return description
    
    def get_publication_type_display(self, obj):
        """Get the display value for publication_type field"""
        if hasattr(obj, 'get_publication_type_display'):
            return obj.get_publication_type_display()
        # Fallback for cases where the method doesn't exist yet
        publication_type_choices = {
            'article': 'Artículo',
            'case': 'Caso',
            'opinion': 'Artículo de Opinión',
            'report': 'Informe',
            'investigation': 'Investigación',
            'news': 'Noticia',
            'video': 'Vídeo',
            'other': 'Otro',
        }
        return publication_type_choices.get(obj.publication_type, obj.publication_type or 'Artículo')
    
    class Meta:
        model = CorruptionCase
        fields = [
            'id', 'title', 'slug', 'short_description', 'full_description', 'processed_description',
            'date', 'amount', 'amount_display', 'total_amount', 'years_duration', 
            'main_image', 'political_party', 'institution', 'corruption_type', 
            'region', 'country', 'tags', 'case_images', 'publication_type', 'publication_type_display', 
            'author_name', 'external_url', 'is_annual_amount', 'start_date', 'sources', 'is_featured', 
            'created_at', 'updated_at'
        ] 