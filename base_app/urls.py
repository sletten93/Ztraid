from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.UsersAPIViewSet.as_view() ),
]
