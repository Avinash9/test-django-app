from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from models import LogUser,Logs
import json
from django.http import HttpResponse


@csrf_exempt
def create_new_entity(request,user_id):
    if request.META.get('REQUEST_METHOD') == 'POST':
        response=create_entry(request.body,user_id)
    elif request.META.get('REQUEST_METHOD') == 'GET':
        response=get_details(request,user_id)
    return HttpResponse(json.dumps(response), content_type="application/json")



def create_entry(data,user_id):
    data = json.loads(data)
    message = data['message']
    time_stamp = data['time_stamp']
    is_sent = data['is_sent']
    try:
        log_user = LogUser.objects.create(id=user_id)
    except Exception as ex:
        log_user = LogUser.objects.get(id=user_id)
    logs= Logs.objects.create(message=message,time_stamp=time_stamp,is_sent=is_sent,
                              logs=log_user)
    logs.save()
    return {"log_id":logs.id}


def get_details(request,user_id):
    offset = int(request.GET.get('start', 0))
    limit=int(request.GET.get('limit',10))
    logs = Logs.objects.filter(logs=user_id).order_by('-time_stamp')
    total_records = logs.count()
    logs = logs[offset:(offset + limit)]
    data=[]
    for row in logs:
        temp = {}
        temp['message']=row.message
        temp['time_stamp']=str(row.time_stamp)
        temp['is_sent']=row.is_sent
        temp['user']= row.logs.id
        data.append(temp)
    return {'data':data,'total_records':total_records}





