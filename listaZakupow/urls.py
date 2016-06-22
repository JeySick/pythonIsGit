from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_listas, name='show_listas'),
    url(r'^lista/(?P<pk>[0-9]+)/$', views.edit_lista, name='edit_lista'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    

]
