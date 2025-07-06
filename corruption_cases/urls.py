from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'political-parties', views.PoliticalPartyViewSet)
router.register(r'institutions', views.InstitutionViewSet)
router.register(r'corruption-types', views.CorruptionTypeViewSet)
router.register(r'regions', views.RegionViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'cases', views.CorruptionCaseViewSet)
router.register(r'case-images', views.CaseImageViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
] 