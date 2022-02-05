from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from vpsHandler.serializers import vpsSerializer, vpsUpdateSerializer
from .models import VPS

class vpsCreate(CreateAPIView):
    queryset = VPS.objects.all()
    serializer_class = vpsSerializer

    def create(self, request, *args, **kwargs):
        if len(request.data['uid']) > 12:
            return Response({"message": "failed", "details": "'uid' value can only be 12 digits long."})
        elif not request.data['uid'].isdigit():
            return Response({"message": "failed", "details": "'uid' value can only contain digits."})
        elif not request.data['cpu'].isdigit():
            return Response({"message": "failed", "details": "'cpu' value must be a number."})
        elif not request.data['ram'].isdigit():
            return Response({"message": "failed", "details": "'ram' value must be a number."})
        elif not request.data['hdd'].isdigit():
            return Response({"message": "failed", "details": "'hdd' value value must be a number."})
        elif len(request.data['cpu']) > 10:
            return Response({"message": "failed", "details": "'cpu' value value must be a number."})
        elif len(request.data['ram']) > 10:
            return Response({"message": "failed", "details": "'ram' value value must be a number."})
        elif len(request.data['hdd']) > 10:
            return Response({"message": "failed", "details": "'hdd' value can only be 10 digits long."})
        elif request.data['status'] not in ['started', 'stopped', 'blocked']:
            return Response({"message": "failed", "details": "Server status can be only 'blocked', 'stopped' or 'started'"})

        serializer = vpsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class vpsShow(ListAPIView):
    serializer_class = vpsSerializer
    def get_queryset(self):
        if not self.request.query_params:
            return VPS.objects.all()

        params = [None,None,None,None,None]
        params[0] = self.request.query_params.get('uid', None)
        params[1] = self.request.query_params.get('cpu', None)
        params[2] = self.request.query_params.get('ram', None)
        params[3] = self.request.query_params.get('hdd', None)
        params[4] = self.request.query_params.get('status', None)
        results = VPS.objects.all()
        results = results.filter(uid__iexact=params[0]) if params[0] else results
        results = results.filter(cpu__iexact=params[1]) if params[1] else results
        results = results.filter(ram__iexact=params[2]) if params[2] else results
        results = results.filter(hdd__iexact=params[3]) if params[3] else results
        results = results.filter(status__iexact=params[4]) if params[4] else results

        return results

class vpsRetrieve(RetrieveAPIView):
    queryset = VPS.objects.all()
    serializer_class = vpsSerializer

class vpsUpdate(RetrieveUpdateAPIView):
    queryset = VPS.objects.all()
    serializer_class = vpsUpdateSerializer

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if request.data['status'] not in ['started', 'stopped', 'blocked']:
            return Response({"message": "failed", "details": "Server status can be only 'Blocked', 'Stopped' or 'Open'"})

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "status updated successfully"})
        else:
            return Response({"message": "failed", "details": serializer.errors})
