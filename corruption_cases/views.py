from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Sum, Count
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse
from django.template.loader import render_to_string

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
    ).prefetch_related('tags', 'case_images')
    lookup_field = 'slug'
    
    # Enable pagination for this viewset
    pagination_class = PageNumberPagination
    
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
        """Get featured corruption cases (only cases, not other publications)"""
        featured_cases = self.queryset.filter(is_featured=True, publication_type='case')
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
        """Get corruption statistics (only for cases, not other publications)"""
        cases_only = self.queryset.filter(publication_type='case')
        total_cases = cases_only.count()
        # Calculate total amount considering annual payments
        total_amount = 0
        for case in cases_only:
            total_amount += case.get_total_amount()
        featured_count = cases_only.filter(is_featured=True).count()
        
        # Cases by political party
        party_stats = cases_only.values('political_party__name').annotate(
            count=Count('id'),
            total_amount=Sum('amount')
        ).order_by('-count')
        
        # Cases by institution type
        institution_stats = cases_only.values('institution__institution_type').annotate(
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

    @action(detail=False, methods=['get'])
    def publications(self, request):
        """Get all publications (exclude cases)"""
        publications = self.queryset.exclude(publication_type='case')
        serializer = self.get_serializer(publications, many=True)
        return Response(serializer.data)

class CaseImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CaseImage.objects.all()
    serializer_class = CaseImageSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['case']
    ordering_fields = ['order', 'created_at']
    ordering = ['order', 'created_at']


def case_detail_view(request, slug):
    """
    Render case detail page with proper meta tags for social media sharing.
    This view is specifically for social media crawlers and SEO.
    """
    try:
        case = get_object_or_404(CorruptionCase, slug=slug)
        
        # Prepare meta tag data with proper image URL
        if case.main_image:
            # Build absolute URL for the image
            image_url = request.build_absolute_uri(case.main_image.url)
        else:
            # Fallback to logo
            image_url = request.build_absolute_uri('/static/logodegu.png')
        
        meta_data = {
            'title': f"{case.title} - D.E.GU",
            'description': case.short_description or 'Caso de corrupción y auditoría del dinero público',
            'image': image_url,
            'url': f"https://degu.es/app/case/{case.slug}",
            'type': 'article',
            'site_name': 'D.E.GU',
            'case': case
        }
        
        # Render the HTML with meta tags
        html_content = render_to_string('case_detail.html', meta_data)
        return HttpResponse(html_content, content_type='text/html')
        
    except CorruptionCase.DoesNotExist:
        # Return 404 with basic meta tags
        meta_data = {
            'title': 'Caso no encontrado - Auditando Impuestos',
            'description': 'El caso solicitado no fue encontrado',
            'image': request.build_absolute_uri('/static/logodegu.png'),
            'url': request.build_absolute_uri(),
            'type': 'website',
            'site_name': 'Auditando Impuestos'
        }
        html_content = render_to_string('case_detail.html', meta_data)
        return HttpResponse(html_content, content_type='text/html', status=404)
    except Exception as e:
        # Return error with basic meta tags
        meta_data = {
            'title': 'Error - Auditando Impuestos',
            'description': 'Ha ocurrido un error al cargar el caso',
            'image': request.build_absolute_uri('/static/logodegu.png'),
            'url': request.build_absolute_uri(),
            'type': 'website',
            'site_name': 'Auditando Impuestos'
        }
        html_content = render_to_string('case_detail.html', meta_data)
        return HttpResponse(html_content, content_type='text/html', status=500)
