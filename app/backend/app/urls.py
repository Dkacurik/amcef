from django.conf import settings
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from django.conf.urls.static import static

from app.intro.viewsets import PostViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Intro API",
        default_version='v1',
        description="",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
                  path('api/', include(router.urls)),
                  path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0)),
                  path('api/redoc', schema_view.with_ui('redoc', cache_timeout=0)),
                  re_path('api/swagger/openapi(?P<format>\\.json|\\.yaml)$', schema_view.without_ui(),
                          name='schema-json'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
