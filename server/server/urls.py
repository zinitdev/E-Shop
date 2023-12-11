from django.contrib import admin
from django.urls import path, include
from server import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
