from rest_framework import serializers
from .models import (
    PoliticalParty, Institution, CorruptionType, Region, 
    Tag, CorruptionCase, ImagenPublicacion
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

class ImagenPublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenPublicacion
        fields = ['id', 'imagen', 'titulo', 'orden', 'fecha_creacion']

class CorruptionCaseListSerializer(serializers.ModelSerializer):
    """Serializer for list view - includes basic info"""
    partido_politico = PoliticalPartySerializer(read_only=True)
    institucion = InstitutionSerializer(read_only=True)
    tipo_corrupcion = CorruptionTypeSerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    etiquetas = TagSerializer(many=True, read_only=True)
    amount_display = serializers.CharField(source='get_amount_display', read_only=True)
    total_amount = serializers.DecimalField(source='get_total_amount', max_digits=20, decimal_places=2, read_only=True)
    years_duration = serializers.IntegerField(source='get_years_duration', read_only=True)
    publication_type_display = serializers.SerializerMethodField(read_only=True)
    
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
        return publication_type_choices.get(obj.tipo_publicacion, obj.tipo_publicacion or 'Artículo')
    
    class Meta:
        model = CorruptionCase
        fields = [
            'id', 'titulo', 'slug', 'descripcion_corta', 'fecha', 'importe', 
            'amount_display', 'total_amount', 'years_duration', 'imagen_principal', 
            'partido_politico', 'institucion', 'tipo_corrupcion', 'region', 'etiquetas', 
            'tipo_publicacion', 'publication_type_display', 'nombre_autor', 
            'url_externa', 'es_importe_anual', 'fecha_inicio', 'es_destacado', 'fecha_creacion'
        ]

class CorruptionCaseDetailSerializer(serializers.ModelSerializer):
    """Serializer for detail view - includes all info"""
    partido_politico = PoliticalPartySerializer(read_only=True)
    institucion = InstitutionSerializer(read_only=True)
    tipo_corrupcion = CorruptionTypeSerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    etiquetas = TagSerializer(many=True, read_only=True)
    imagenes = ImagenPublicacionSerializer(many=True, read_only=True)
    amount_display = serializers.CharField(source='get_amount_display', read_only=True)
    total_amount = serializers.DecimalField(source='get_total_amount', max_digits=20, decimal_places=2, read_only=True)
    years_duration = serializers.IntegerField(source='get_years_duration', read_only=True)
    publication_type_display = serializers.SerializerMethodField(read_only=True)
    processed_description = serializers.CharField(source='get_processed_description', read_only=True)
    
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
        return publication_type_choices.get(obj.tipo_publicacion, obj.tipo_publicacion or 'Artículo')
    
    class Meta:
        model = CorruptionCase
        fields = [
            'id', 'titulo', 'slug', 'descripcion_corta', 'descripcion_completa', 'processed_description',
            'fecha', 'importe', 'amount_display', 'total_amount', 'years_duration', 
            'imagen_principal', 'partido_politico', 'institucion', 'tipo_corrupcion', 
            'region', 'etiquetas', 'imagenes', 'tipo_publicacion', 'publication_type_display', 
            'nombre_autor', 'url_externa', 'es_importe_anual', 'fecha_inicio', 'fuentes', 'es_destacado', 
            'fecha_creacion', 'fecha_actualizacion'
        ] 