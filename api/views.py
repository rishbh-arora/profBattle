from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Faculty
from .serializers import FacSerializer
from rest_framework import permissions, authentication
from django_filters.rest_framework import DjangoFilterBackend

class FacViewset(ReadOnlyModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = HistoryFilter