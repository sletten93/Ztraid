from django.urls import path
from . import views

urlpatterns = [
    path('api/Users/', views.UsersViewSet.as_view()),
]
