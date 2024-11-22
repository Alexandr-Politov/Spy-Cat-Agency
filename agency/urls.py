from django.urls import path, include
from rest_framework.routers import DefaultRouter
from agency.views import SpyCatViewSet, MissionViewSet


router = DefaultRouter()
router.register("spycats", SpyCatViewSet, basename="spycat"),
router.register("missions", MissionViewSet, basename="mission")


app_name = "agency"

urlpatterns = [
    path("", include(router.urls)),
]
