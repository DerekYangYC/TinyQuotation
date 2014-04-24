from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from quotation import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'register/', views.register, name='register'),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

