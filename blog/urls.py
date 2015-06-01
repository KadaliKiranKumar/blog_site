from django.conf.urls import url
from blog.views import ViaDashboardView

from . import views

urlpatterns = [
    url(r'^jobs/(?P<pk>\d+)/?$', views.index, {'w':123}, name='index'),
    
    url(r'^$', ViaDashboardView.as_view(), name='blog'),
]