from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from geekshop.views import index, contacts, ErrorPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('mainapp.urls', namespace='products'), name='products'),
    path('admin_staff/', include('adminapp.urls', namespace='admin_staff'), name='admin_staff'),
    path('auth/', include('authapp.urls', namespace='auth'), name='auth'),
    path('basket/', include('basketapp.urls', namespace='basket'), name='basket'),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('', include('social_django.urls', namespace='social')),
    url(r'^error_page/$', ErrorPage.as_view(), name="error-page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
