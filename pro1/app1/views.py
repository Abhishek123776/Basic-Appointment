from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from . models import Appointment
from . serializers import AppointmentSerializer
# Create your views here.

class AppointmentViewset(viewsets.ViewSet):
    def create(self,request):
        serializer=AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def list(self,request):
        objs=Appointment.objects.all()
        serializer=AppointmentSerializer(objs,many=True)
        return Response(data=serializer.data)

    def retrieve(self,request,pk=None):
        obj=get_object_or_404(Appointment,id=pk)
        serializer=AppointmentSerializer(obj)
        return Response(data=serializer.data)
    
    def update(self,request,pk=None):
        obj=get_object_or_404(Appointment,id=pk)
        serializer=AppointmentSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def partial_update(self,request,pk=None):
        obj=get_object_or_404(Appointment,id=pk)
        serializer=AppointmentSerializer(instance=obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def destroy(self,request,pk=None):
        obj=get_object_or_404(Appointment,id=pk)
        obj.delete()
        return Response(data={"msg":'DATA DELETED SUCCESSFULY'})