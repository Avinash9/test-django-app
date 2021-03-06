


from models import Logs,LogUser
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie import fields


class UserResource(ModelResource):

    class Meta:
        queryset = LogUser.objects.all()
        resource_name = 'user'





class LogResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)

    class Meta:
        queryset = Logs.objects.all().order_by('-time_stamp')
        resource_name = 'chatserver'
        always_return_data = True
        authentication = Authentication()
        authorization = Authorization()
        list_allowed_methods = ['get','post','put']

    # def pre
    #
    # def obj_create(self, bundle, **kwargs):
    #     print ":::::::::",kwargs
    #     print ":::::::::::::::::"



