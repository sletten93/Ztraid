from base_app import views
from rest_framework import routers
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView


# Ändrar, vid körning, namn och beskrivning av API-förstasidan
class Router(routers.DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        root_view = super(Router, self).get_api_root_view(api_urls=api_urls)
        root_view.cls.__name__ = "Hey, you. You're finally awake."
        root_view.cls.__doc__ = "You were trying to cross the border, right?"
        return root_view


router = Router()
router.register(r'users', views.UsersViewSet)
router.register(r'FAQ', views.FAQViewSet)
router.register(r'paragraphs', views.ParagraphViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'devices', views.DevicesViewSet)
router.register(r'userPrefs', views.UserPrefViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', include('django.contrib.auth.urls')),
    path('', include('frontend.urls')),
    #   path('', include('base_app.urls')),
    #   path('', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(template_name=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
