
from django.conf.urls import include, url

from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexPostView.as_view(), name='index_posts'),
    url(r'^(?P<pk>[0-9]+)/$', views.ReadPostView.as_view(), name='read_post'),
    url(r'^(?P<pk>[0-9]+)/update_post/$', views.UpdatePostView.as_view(), name='update_post'),
    url(r'^createPost/$', views.PostCreateView.as_view(), name='create_post'),
    url(r'^(?P<pk>[0-9]+)/delete_post/$', views.PostDeleteView.as_view(), name='delete_post'),

]

