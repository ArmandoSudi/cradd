from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from website import views

app_name = 'website'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^blog/$', views.article_list, name='article_list'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^team/$', views.team, name='team'),
    url(r'^blog/(?P<article_id>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^message/', views.get_message, name='get_message'),
    url(r'^language/', views.toggle_language, name='toggle_language'),
    url(r'^projects/', views.project_list, name='project_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
