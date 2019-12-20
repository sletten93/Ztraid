from base_app import views
from rest_framework import routers
from django.urls import include
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'Users', views.ZtrUserViewSet)
router.register(r'FAQ', views.FAQViewSet)
router.register(r'Paragraphs', views.ParagraphViewSet)
router.register(r'Products', views.ProductViewSet)
router.register(r'Devices', views.DevicesViewSet)
router.register(r'UserPrefs', views.UserPrefViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
