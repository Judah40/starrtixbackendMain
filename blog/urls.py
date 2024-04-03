from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import blogViewSet

router=DefaultRouter()
router.register(r'blog',blogViewSet)

urlpatterns = [
    path('', include(router.urls))
]
