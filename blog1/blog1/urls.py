from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from posts.views import IndexListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexListView.as_view(), name='index'),
    path('accounts/', include('accounts.urls')),
    path('post/', include('posts.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)