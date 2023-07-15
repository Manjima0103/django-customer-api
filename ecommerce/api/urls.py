from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProductViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
