from django.conf.urls import patterns, include, url
from django.contrib import admin


from tastypie.api import Api
from polls.resource import LogResource

v1_api = Api(api_name='v1')
v1_api.register(LogResource())

urlpatterns = patterns('',
    # Examples:
    url(r'^chat/(?P<user_id>[0-9a-zA-Z\-]+)$', 'polls.views.create_new_entity', name='create_new_entity'),
    # url(r'^blog/', include('blog.urls')),
    (r'^', include(v1_api.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
