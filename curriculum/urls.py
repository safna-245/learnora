from django.urls import path

from curriculum.views import CourseCreateView
from curriculum.views import CourseListView
from curriculum.views import CourseRetrieveView
from curriculum.views import CourseUpdateView
from curriculum.views import CourseDeleteView

urlpatterns=[
    path("create/",CourseCreateView.as_view()),
    path("all/",CourseListView.as_view()),
    path("<int:pk>/",CourseRetrieveView.as_view()),
    path("update/<int:pk>/",CourseUpdateView.as_view()),
    path("delete/<int:pk>/",CourseDeleteView.as_view()),
]