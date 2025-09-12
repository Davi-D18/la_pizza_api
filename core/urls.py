from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/v1/', include('apps.nome-app.urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(), name="schema-swagger-ui"),
]

# Debug Toolbar URLs (apenas em desenvolvimento)
if settings.DEBUG:
    try:
        import debug_toolbar

        urlpatterns += [
            path("debug/", include(debug_toolbar.urls)),
        ]
    except ImportError:
        pass
