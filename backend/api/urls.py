from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet

router_v_1 = DefaultRouter()
router_v_1.register('employees', EmployeeViewSet, basename='employees')


urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path("", include(router_v_1.urls)),
]
