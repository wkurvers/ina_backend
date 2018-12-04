from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
import json
from ina_api.models import *
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def getUserById(request, id):
    try:
        userObject = User.objects.get(pk=id).__repr__()
        return JsonResponse({"bool": True, "msg": "User did exist", "user": userObject}, safe=True)
    except ObjectDoesNotExist:
        return JsonResponse({"bool": False, "msg": "User did not exist"}, safe=True)


@require_http_methods(['POST'])
def createUser(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        userObject = User(email=data['email'], password=data['password'], first_name=data['firstName'],
                          last_name=data['lastName'], bio=data['bio'], mobile=data['mobile'],
                          organisation=data['organisation'], function=data['function'],
                          profile_photo_path=data['profilePhotoPath'])
        userObject.save()
        
        return JsonResponse({"bool": True, "msg": "User entry created", "id": userObject.pk}, safe=True)
    except:
        return JsonResponse({"bool": False, "msg": "Could not create entry"}, safe=True)


@require_http_methods(['PUT'])
def updateUser(request):
    data = json.loads(request.body.decode('utf8'))

    try:
        userObject = User.objects.get(pk=data['id'])
    except:
        return JsonResponse({"bool": False, "msg": "User with id [" + str(data['id']) + "] does not exist"}, safe=True)
    try:
        userObject.bio = data['bio']
        userObject.organisation = data['organisation']
        userObject.function = data['function']
        userObject.save()

        return JsonResponse({"bool": True, "msg": "User entry updated"}, safe=True)
    except:
        return JsonResponse({"bool": False, "msg": "User entry could not be updated"}, safe=True)


@require_http_methods(['DELETE'])
def deleteUser(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        userObject = User.objects.get(pk=data['id'])
    except:
        return JsonResponse({"bool": False, "msg": "User with id [" + str(data['id']) + "] does not exist"}, safe=True)
    try:
        userObject.delete()
        return JsonResponse({"bool": True, "msg": "User entry deleted"}, safe=True)
    except:
        return JsonResponse({"bool": False, "msg": "User entry could not be deleted"}, safe=True)
