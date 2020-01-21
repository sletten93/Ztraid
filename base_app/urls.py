from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.UsersViewSet.as_view({'get': 'list'}) ),
]
