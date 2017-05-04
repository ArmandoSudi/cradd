from django.conf.urls import url
from website import views

app_name = 'website'
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^hello/', views.hello, name='hello'),
    url(r'^home/', views.home, name='home'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^message/', views.get_message, name='get_message'),
    url(r'^test/', views.test, name='test'),
]
