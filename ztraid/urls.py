from base_app import views
from rest_framework import routers
from django.urls import include
from django.contrib import admin
from django.urls import path


# Ändrar, vid körning, namn och beskrivning av API-förstasidan
class Router(routers.DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        root_view = super(Router, self).get_api_root_view(api_urls=api_urls)
        root_view.cls.__name__ = "Hey, you. You're finally awake."
        root_view.cls.__doc__ = "You were trying to cross the border, right?"
        return root_view


router = Router()
router.register(r'Users', views.UsersViewSet)
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