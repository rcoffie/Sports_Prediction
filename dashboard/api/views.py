from rest_framework.viewsets import ModelViewSet
from .serializers import ReadDataSerializer, WriteDataSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from dashboard.models import Data


class DataViewSet(ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = ReadDataSerializer

    def get_serializer_class(self):
        if self.action in ('list','retrieve'):
            return ReadDataSerializer
        return WriteDataSerializer
