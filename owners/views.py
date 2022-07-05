
import json
from django.http import JsonResponse

from django.shortcuts import render
from django.views import View

from owners.models import Owner, Dog
# Create your views here.


class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(
            name=data['name'],
            email=data['email'],
            age=data['age'])
        return JsonResponse({'message': 'created'}, status=201)


class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(
            name=data['name'],
            age=data['age'],
            owner=Owner.objects.get(name=data['owner'])
        )
        return JsonResponse({'message': 'created'}, status=201)
