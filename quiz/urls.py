from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^', include(('users.urls','users'), namespace="users")),

    url(r'^app/accounts/', include('registration.backends.default.urls')),

    url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_FILE_ROOT}),
]
