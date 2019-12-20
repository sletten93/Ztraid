from Ztraid.testApp import views
from rest_framework import routers
from django.urls import include, path
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'users', views.ZtrUserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'FAQ', views.FAQViewSet)
router.register(r'Paragraph', views.ParagraphViewSet)
router.register(r'Product', views.ProductViewSet)
router.register(r'Devices', views.DevicesViewSet)
router.register(r'UserPref', views.UserPrefViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
