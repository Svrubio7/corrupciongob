"""
URL configuration for corruption_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from corruption_cases.views import publication_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('corruption_cases.urls')),
    # Social media crawler routes - must be before catch-all
    path('app/case/<slug:slug>/', publication_detail_view, name='case-detail-meta'),
    path('app/publicacion/<slug:slug>/', publication_detail_view, name='publicacion-detail-meta'),
    # Vue SPA catch-all route - must be last
    re_path(r'^(?!static/|media/|admin/|api/).*$', TemplateView.as_view(template_name="index.html")),
]

# This must be after the above
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)