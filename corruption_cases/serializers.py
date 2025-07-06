from rest_framework import serializers
from .models import (
    PoliticalParty, Institution, CorruptionType, Region, 
    Tag, CorruptionCase, CaseImage
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

class CaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseImage
        fields = ['id', 'image', 'caption', 'order', 'created_at']

class CorruptionCaseListSerializer(serializers.ModelSerializer):
    """Serializer for list view - includes basic info"""
    political_party = PoliticalPartySerializer(read_only=True)
    institution = InstitutionSerializer(read_only=True)
    corruption_type = CorruptionTypeSerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    amount_display = serializers.CharField(source='get_amount_display', read_only=True)
    
    class Meta:
        model = CorruptionCase
        fields = [
            'id', 'title', 'slug', 'short_description', 'date', 'amount', 
            'amount_display', 'main_image', 'political_party', 'institution', 
            'corruption_type', 'region', 'tags', 'is_featured', 'created_at'
        ]

class CorruptionCaseDetailSerializer(serializers.ModelSerializer):
    """Serializer for detail view - includes all info"""
    political_party = PoliticalPartySerializer(read_only=True)
    institution = InstitutionSerializer(read_only=True)
    corruption_type = CorruptionTypeSerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    images = CaseImageSerializer(many=True, read_only=True)
    amount_display = serializers.CharField(source='get_amount_display', read_only=True)
    
    class Meta:
        model = CorruptionCase
        fields = [
            'id', 'title', 'slug', 'short_description', 'full_description', 
            'date', 'amount', 'amount_display', 'main_image', 'political_party', 
            'institution', 'corruption_type', 'region', 'tags', 'images', 
            'sources', 'is_featured', 'created_at', 'updated_at'
        ] 