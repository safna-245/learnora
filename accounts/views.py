from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from accounts.models import User
from accounts.models import TrainerProfile

from accounts.serializers import UserSerializer
from accounts.serializers import TrainerProfileSerializer

from accounts.permissions import IsTrainerUser

# Create your views here.

class StudentCreateView(APIView):

    def post(self,request):
        form_data = request.data
        
        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(role="student",**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class TrainerCreateView(APIView):

    def post(self,request):
        form_data = request.data
        
        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            instance = User.objects.create_user(role="trainer",**cleaned_data)

            serializer_instance = UserSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


class TrainerProfileUpdateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsTrainerUser]

    def put(self,request):

        form_data = request.data

        trainer_profile_object = TrainerProfile.objects.get(user=request.user)

        serializer_instance = TrainerProfileSerializer(data=form_data,instance=trainer_profile_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data) 

        else:

            return Response(data=serializer_instance.errors) 


class TrainerProfileDetailView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated, IsTrainerUser]

    def get(self, request):

        trainer_profile_object = TrainerProfile.objects.get(user=request.user)

        serializer_instance = TrainerProfileSerializer(trainer_profile_object)

        return Response(data=serializer_instance.data)