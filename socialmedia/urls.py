from django.contrib import admin
from rest_framework import permissions
from django.urls import path, include,re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Social Media App API",
        default_version='v1',
        description="Simple social media app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="saalehmohamedd@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Posts.urls')),
    path('api/',include('Likes.urls')),
    path('api/',include('Comments.urls')),
    path('api/',include('Users.urls')),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]