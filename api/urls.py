from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ListViewSet


router = SimpleRouter()
router.register(r'list', ListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]