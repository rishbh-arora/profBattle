from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Faculty
from .serializers import FacSerializer, UserSerializer
from rest_framework import permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import action
import random
from django.core.paginator import Paginator
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination

class FacViewset(ReadOnlyModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    @action(detail=False, methods=['get'])
    def random(self, request):
        num_random_elements = 10
        total_records = Faculty.objects.count()
        random_indices = random.sample(range(total_records), num_random_elements)
        random_elements = []
        for index in random_indices:
            paginator = Paginator(Faculty.objects.all(), 1)
            random_elements.append(paginator.page(index + 1).object_list[0])
        serializer = self.get_serializer(random_elements, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        key = request.query_params.get('name', None)
        fac = self.get_queryset().filter(name__icontains=key)

        # Apply pagination
        paginator = PageNumberPagination()
        paginated_fac = paginator.paginate_queryset(queryset=fac, request=request, view=self)
        
        # Serialize the paginated queryset
        serializer = self.get_serializer(paginated_fac, many=True)
        return paginator.get_paginated_response(serializer.data)


class UserViewset(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]