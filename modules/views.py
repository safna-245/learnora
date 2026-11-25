from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from modules.models import Module
from modules.serializers import ModuleSerializer
from modules.permissions import IsCourseOwner

from curriculum.models import Course

# Create your views here.
class ModuleCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsCourseOwner]

    def post(self,request,pk=None):

        course_id = pk

        course_object = Course.objects.get(id=course_id)

        form_data = request.data

        serializer_instance= ModuleSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(course = course_object)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


class ModuleRetrieveView(RetrieveAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ModuleSerializer

    queryset = Module.objects.all()

class ModuleUpdateView(UpdateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsCourseOwner]

    serializer_class = ModuleSerializer

    queryset = Module.objects.all()

class ModuleDeleteView(DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsCourseOwner]

    serializer_class = ModuleSerializer

    queryset = Module.objects.all()
