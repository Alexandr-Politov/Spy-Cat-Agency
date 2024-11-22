from rest_framework.viewsets import ModelViewSet
from agency.models import SpyCat, Mission
from agency.serializers import SpyCatSerializer, MissionSerializer


class SpyCatViewSet(ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer


class MissionViewSet(ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
