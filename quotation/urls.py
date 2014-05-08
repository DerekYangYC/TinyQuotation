from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from quotation import views

#$ should be used to avoid the behavior under the same parent path. Like login/ and login/submit/
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'register/submit/$', views.register_submit, name='register_submit'),
    url(r'register/$', views.register, name='register'),
    url(r'logout/$', views.logout, name='logout'),
    url(r'login/$', views.login, name='login'),
    url(r'login/submit/$', views.login_submit, name='login_submit'),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

