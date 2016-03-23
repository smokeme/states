from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from main import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'states.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^state_view/(?P<name>.+)/$', 'main.views.state_view'),
    url(r'^state_list/$', 'main.views.state_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_search/', 'main.views.get_search'),
    url(r'^get_post/', 'main.views.get_post'),
    url(r'^index.html', 'main.views.template_view'),
    url(r'^detail.html/(?P<name>.+)/$', 'main.views.details_view'),
    url(r'^about.html$', TemplateView.as_view(template_name='about.html'), name='home'),
    #req views
    url(r'^cbv_list/', views.StateListView.as_view()),
    url(r'^cbv_detail/(?P<pk>[0-9]+)/$', views.StateDetailView.as_view()),
    url(r'^city_search/$', 'main.views.city_search'),
    url(r'^city_create/$', 'main.views.city_create'),
    url(r'^city_delete/(?P<pk>[0-9]+)/$', 'main.views.city_delete'),
    url(r'^city_edit/(?P<pk>[0-9]+)/$', 'main.views.city_edit'),
]
