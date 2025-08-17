from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Sum, Count
from django.utils import timezone
from datetime import timedelta

from .models import (
    PoliticalParty, Institution, CorruptionType, Region, 
    Tag, CorruptionCase, CaseImage
)
from .serializers import (
    PoliticalPartySerializer, InstitutionSerializer, CorruptionTypeSerializer,
    RegionSerializer, TagSerializer, CaseImageSerializer,
    CorruptionCaseListSerializer, CorruptionCaseDetailSerializer
)

class PoliticalPartyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PoliticalParty.objects.all()
    serializer_class = PoliticalPartySerializer
    pagination_class = None
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'short_name']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class InstitutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['institution_type', 'region']
    search_fields = ['name', 'region']
    ordering_fields = ['name', 'institution_type', 'created_at']
    ordering = ['name']

class CorruptionTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CorruptionType.objects.all()
    serializer_class = CorruptionTypeSerializer
    pagination_class = None
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['autonomous_community']
    search_fields = ['name', 'autonomous_community']
    ordering_fields = ['name', 'autonomous_community', 'created_at']
    ordering = ['name']

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class CorruptionCaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CorruptionCase.objects.select_related(
        'political_party', 'institution', 'corruption_type', 'region'
    ).prefetch_related('tags', 'images')
    lookup_field = 'slug'
    
    # Disable pagination for this viewset
    pagination_class = None
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'date': ['exact', 'gte', 'lte', 'range'],
        'amount': ['exact', 'gte', 'lte', 'range'],
        'political_party': ['exact'],
        'institution': ['exact'],
        'corruption_type': ['exact'],
        'region': ['exact'],
        'is_featured': ['exact'],
        'tags': ['exact'],
    }
    search_fields = ['title', 'short_description', 'full_description']
    ordering_fields = ['date', 'amount', 'title', 'created_at']
    ordering = ['-date', '-created_at']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CorruptionCaseDetailSerializer
        return CorruptionCaseListSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured corruption cases"""
        featured_cases = self.queryset.filter(is_featured=True)
        serializer = self.get_serializer(featured_cases, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Get recent corruption cases (last 30 days)"""
        thirty_days_ago = timezone.now().date() - timedelta(days=30)
        recent_cases = self.queryset.filter(date__gte=thirty_days_ago)
        serializer = self.get_serializer(recent_cases, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get corruption statistics"""
        total_cases = self.queryset.count()
        total_amount = self.queryset.aggregate(total=Sum('amount'))['total'] or 0
        featured_count = self.queryset.filter(is_featured=True).count()
        
        # Cases by political party
        party_stats = self.queryset.values('political_party__name').annotate(
            count=Count('id'),
            total_amount=Sum('amount')
        ).order_by('-count')
        
        # Cases by institution type
        institution_stats = self.queryset.values('institution__institution_type').annotate(
            count=Count('id'),
            total_amount=Sum('amount')
        ).order_by('-count')
        
        return Response({
            'total_cases': total_cases,
            'total_amount': total_amount,
            'featured_count': featured_count,
            'party_statistics': party_stats,
            'institution_statistics': institution_stats,
        })

    @action(detail=False, methods=['get'])
    def search(self, request):
        """Advanced search endpoint"""
        query = request.query_params.get('q', '')
        if not query:
            return Response({'error': 'Query parameter "q" is required'}, status=400)
        
        # Search in multiple fields
        search_query = Q(title__icontains=query) | \
                      Q(short_description__icontains=query) | \
                      Q(full_description__icontains=query) | \
                      Q(political_party__name__icontains=query) | \
                      Q(institution__name__icontains=query) | \
                      Q(corruption_type__name__icontains=query) | \
                      Q(region__name__icontains=query) | \
                      Q(tags__name__icontains=query)
        
        search_results = self.queryset.filter(search_query).distinct()
        serializer = self.get_serializer(search_results, many=True)
        return Response(serializer.data)

class CaseImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CaseImage.objects.all()
    serializer_class = CaseImageSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['case']
    ordering_fields = ['order', 'created_at']
    ordering = ['order', 'created_at']
