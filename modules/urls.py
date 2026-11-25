from django.urls import path
from modules.views import ModuleCreateView
from modules.views import ModuleRetrieveView
from modules.views import ModuleUpdateView
from modules.views import ModuleDeleteView

urlpatterns = [
    path('course/<int:pk>/module/', ModuleCreateView.as_view()),
    path('<int:pk>/', ModuleRetrieveView.as_view()),
    path('update/<int:pk>/', ModuleUpdateView.as_view()),
    path('delete/<int:pk>/', ModuleDeleteView.as_view()),
]