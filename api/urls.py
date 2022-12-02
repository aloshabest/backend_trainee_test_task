from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AdvertViewSet


router = SimpleRouter()
router.register(r'list', AdvertViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]