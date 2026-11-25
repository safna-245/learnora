from django.urls import path

from accounts.views import StudentCreateView
from accounts.views import TrainerCreateView
from accounts.views import TrainerProfileUpdateView
from accounts.views import TrainerProfileDetailView

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns=[
    path("student/register/",StudentCreateView.as_view()),
    path("trainer/register/",TrainerCreateView.as_view()),
    path("trainer/profile/",TrainerProfileUpdateView.as_view()),
    path("profile/me/",TrainerProfileDetailView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
]