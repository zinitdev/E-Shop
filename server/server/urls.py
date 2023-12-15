from django.contrib import admin
from django.urls import path, include
from server import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="E-Shop APIs",
        default_version="v1",
        description="Schema Views for E-Shop APIs",
        terms_of_service="https://www.yourapp.com/policies/terms/",
        contact=openapi.Contact(email="zin.it.dev@gmail.com"),
        license=openapi.License(name="MIT License (MIT)"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
