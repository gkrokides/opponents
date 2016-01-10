from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/$',TemplateView.as_view(template_name='opponents/about.html'),name='about'),
    url(r'^contact/$',TemplateView.as_view(template_name='opponents/contact.html'),name='contact'),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]