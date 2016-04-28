


from models import Logs
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization



class LogResource(ModelResource):


    class Meta:
        queryset = Logs.objects.all().order_by('-time_stamp')
        resource_name = 'user'
        always_return_data = True
        authentication = Authentication()
        authorization = Authorization()
        list_allowed_methods = ['get','post','put']




class LogResource(ModelResource):
    user = fields.ForeignKey(QueryTemplateResource, 'resource', full=True)

    class Meta:
        queryset = Logs.objects.all().order_by('-time_stamp')
        resource_name = 'user'
        always_return_data = True
        authentication = Authentication()
        authorization = Authorization()
        list_allowed_methods = ['get','post','put']



