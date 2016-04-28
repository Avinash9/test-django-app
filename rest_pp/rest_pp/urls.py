from django.conf.urls import patterns, include, url
from django.contrib import admin


from tastypie.api import Api
from polls.resource import LogResource

v1_api = Api(api_name='v1')
v1_api.register(LogResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rest_pp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^', include(v1_api.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
