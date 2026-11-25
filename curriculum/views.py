from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveAPIView,ListAPIView,UpdateAPIView,DestroyAPIView

from curriculum.serializers import CourseSerializer
from curriculum.models import Course
from curriculum.permissions import IsOwner

from accounts.permissions import IsTrainerUser
# Create your views here.
class CourseCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsTrainerUser]

    def post(self, request):

        form_data = request.data

        serializer_instance = CourseSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(trainer=request.user)

            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)

class CourseListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CourseSerializer
    
    queryset = Course.objects.all()

    

class CourseRetrieveView(RetrieveAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CourseSerializer

    queryset = Course.objects.all()


class CourseUpdateView(UpdateAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsOwner]

    serializer_class = CourseSerializer

    queryset = Course.objects.all()

class CourseDeleteView(DestroyAPIView):

    authentication_classes=[authentication.TokenAuthentication]
    
    permission_classes = [permissions.IsAuthenticated,IsOwner]

    serializer_class = CourseSerializer

    queryset = Course.objects.all()



