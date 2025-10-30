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
    Tag, Country, CorruptionCase, CaseImage
)
from .serializers import (
    PoliticalPartySerializer, InstitutionSerializer, CorruptionTypeSerializer,
    RegionSerializer, TagSerializer, CountrySerializer, CaseImageSerializer,
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

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = None
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'code']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class CorruptionCaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CorruptionCase.objects.select_related(
        'political_party', 'institution', 'corruption_type', 'region', 'country'
    ).prefetch_related('tags', 'case_images')
    lookup_field = 'slug'
    
    # Enable pagination for this viewset
    pagination_class = PageNumberPagination
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'date': ['exact', 'gte', 'lte', 'range'],
        'publication_date': ['exact', 'gte', 'lte', 'range'],
        'amount': ['exact', 'gte', 'lte', 'range'],
        'political_party': ['exact'],
        'institution': ['exact'],
        'corruption_type': ['exact'],
        'region': ['exact'],
        'country': ['exact'],
        'is_featured': ['exact'],
        'tags': ['exact'],
    }
    search_fields = ['title', 'short_description', 'full_description']
    ordering_fields = ['date', 'publication_date', 'amount', 'title', 'created_at']
    ordering = ['-publication_date', '-date', '-created_at']

    def get_queryset(self):
        """
        Override get_queryset to filter by publication_type.
        - 'list' action: only show cases
        - 'retrieve' action: show any publication type (to allow viewing article details)
        - Custom actions handle their own filtering
        """
        queryset = super().get_queryset()
        
        # Only filter for 'list' action (not 'retrieve' so we can view any publication detail)
        if self.action == 'list':
            queryset = queryset.filter(publication_type='case')
        
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CorruptionCaseDetailSerializer
        return CorruptionCaseListSerializer

    @action(detail=False, methods=['get'], pagination_class=None)
    def featured(self, request):
        """Get featured corruption cases ordered by publication date (only cases, not other publications)"""
        featured_cases = super().get_queryset().filter(
            is_featured=True, 
            publication_type='case'
        ).order_by('-publication_date', '-date', '-created_at')[:3]
        serializer = self.get_serializer(featured_cases, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], pagination_class=None)
    def recent(self, request):
        """Get recent corruption cases ordered by publication date (only cases, not other publications)"""
        recent_cases = super().get_queryset().filter(
            publication_type='case'
        ).order_by('-publication_date', '-date', '-created_at')[:3]
        serializer = self.get_serializer(recent_cases, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], pagination_class=None)
    def statistics(self, request):
        """Get corruption statistics (only for cases, not other publications)"""
        cases_only = super().get_queryset().filter(publication_type='case')
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

    @action(detail=False, methods=['get'], pagination_class=None)
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
        
        search_results = super().get_queryset().filter(search_query, publication_type='case').distinct()
        serializer = self.get_serializer(search_results, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], pagination_class=None)
    def publications(self, request):
        """Get all publications (exclude cases) - no pagination"""
        publications = super().get_queryset().exclude(publication_type='case')
        serializer = self.get_serializer(publications, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], pagination_class=None)
    def by_country(self, request):
        """Get corruption statistics grouped by country with cases"""
        from django.db.models import Count, Sum
        from decimal import Decimal
        
        # Get all countries with cases
        countries_with_cases = Country.objects.filter(
            corruptioncase__isnull=False,
            corruptioncase__publication_type='case'
        ).distinct()
        
        country_data = []
        for country in countries_with_cases:
            cases = super().get_queryset().filter(country=country, publication_type='case')
            
            # Calculate total amount considering annual payments
            total_amount = Decimal('0')
            for case in cases:
                total_amount += case.get_total_amount()
            
            if cases.exists():
                country_data.append({
                    'country': CountrySerializer(country).data,
                    'total_cases': cases.count(),
                    'total_amount': float(total_amount),
                    'cases': CorruptionCaseListSerializer(cases, many=True).data
                })
        
        # Sort by total amount descending
        country_data.sort(key=lambda x: x['total_amount'], reverse=True)
        
        return Response(country_data)

class CaseImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CaseImage.objects.all()
    serializer_class = CaseImageSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['case']
    ordering_fields = ['order', 'created_at']
    ordering = ['order', 'created_at']


def is_crawler(request):
    """
    Detect if the request is from a social media crawler or bot.
    Uses multiple detection methods for reliability.
    """
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    
    # Common crawler/bot keywords
    crawler_keywords = [
        'facebookexternalhit',   # Facebook
        'facebot',               # Facebook
        'twitterbot',            # Twitter/X
        'twitter',               # Twitter variations
        'linkedinbot',           # LinkedIn
        'linkedin',              # LinkedIn variations
        'whatsapp',              # WhatsApp
        'whatsappbot',           # WhatsApp
        'telegrambot',           # Telegram
        'slackbot',              # Slack
        'slack-imgproxy',        # Slack image proxy
        'discordbot',            # Discord
        'pinterestbot',          # Pinterest
        'pinterest',             # Pinterest variations
        'redditbot',             # Reddit
        'tumblr',                # Tumblr
        'skype',                 # Skype
        'googlebot',             # Google
        'bingbot',               # Bing
        'bingpreview',           # Bing preview
        'yandexbot',             # Yandex
        'baiduspider',           # Baidu
        'applebot',              # Apple
        'bot',                   # Generic bot
        'crawler',               # Generic crawler
        'spider',                # Generic spider
        'scraper',               # Generic scraper
        'preview',               # Preview generators
    ]
    
    # Check for crawler keywords
    if any(keyword in user_agent for keyword in crawler_keywords):
        return True
    
    # Check for common non-browser user agents (often used by social media crawlers)
    # If user agent doesn't contain common browser identifiers, it's likely a crawler
    browser_indicators = ['mozilla', 'chrome', 'safari', 'firefox', 'edge', 'opera']
    has_browser_indicator = any(browser in user_agent for browser in browser_indicators)
    
    # If it has no browser indicators but has http/https, it's likely a crawler
    if not has_browser_indicator and ('http' in user_agent or len(user_agent) < 20):
        return True
    
    # Check for headless browsers often used for crawling
    if 'headless' in user_agent or 'phantom' in user_agent or 'selenium' in user_agent:
        return True
    
    return False


def publication_detail_view(request, slug, publication_type='case'):
    """
    Render publication detail page with proper meta tags for social media sharing.
    This view handles both cases and publications.
    Serves dynamic meta tags for crawlers while still loading the Vue app for browsers.
    """
    try:
        publication = get_object_or_404(CorruptionCase, slug=slug)
        
        # Determine the correct URL based on publication type
        if publication.publication_type == 'case':
            url = f"https://degu.es/app/case/{publication.slug}"
        else:
            url = f"https://degu.es/app/publicacion/{publication.slug}"
        
        # Prepare meta tag data with proper image URL
        if publication.main_image:
            # Build absolute URL for the image
            image_url = request.build_absolute_uri(publication.main_image.url)
        else:
            # Fallback to logo
            image_url = request.build_absolute_uri('/static/logodegu.png')
        
        # Detect if this is a crawler/bot
        if is_crawler(request):
            # For crawlers: serve the meta tags template (with proper escaping)
            meta_data = {
                'title': f"{publication.title} - D.E.GU",
                'description': publication.short_description or 'Análisis y auditoría del dinero público',
                'image': image_url,
                'url': url,
                'type': 'article',
                'site_name': 'D.E.GU',
                'case': publication,
                'publication_type': publication.publication_type,
            }
            return render(request, 'case_detail.html', meta_data)
        else:
            # For regular browsers: serve the Vue SPA
            return render(request, 'index.html')
        
    except CorruptionCase.DoesNotExist:
        # Return 404 - serve regular Vue app
        return render(request, 'index.html', status=404)
    except Exception as e:
        # Return error - serve regular Vue app  
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error in publication_detail_view: {str(e)}")
        return render(request, 'index.html', status=500)


def case_detail_view(request, slug):
    """
    Wrapper for case detail view (publication_type='case')
    """
    return publication_detail_view(request, slug, publication_type='case')
