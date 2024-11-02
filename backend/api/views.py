from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response

from reviews.models import Employee

from .permissions import CreatePermission, DeletePermission, PutPermission
from .serializers import ReadEmployeeSerializer, WriteEmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = ReadEmployeeSerializer
    http_method_names = ['get', 'list', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_fired',]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ReadEmployeeSerializer
        return WriteEmployeeSerializer

    @action(detail=False, methods=['post'],
            permission_classes=(CreatePermission,))
    def create_employee(self, request):
        serializer = WriteEmployeeSerializer(
            data=request.data,
            context={'request': request},
            partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'],
            permission_classes=(PutPermission,))
    def change_employee(self, request, pk=None):
        serializer = WriteEmployeeSerializer(
            data=request.data,
            context={'request': request},
            partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['delete'],
            permission_classes=(DeletePermission,))
    def delete_employee(self, request, pk=None):
        obj = get_object_or_404(Employee, id=pk)
        obj.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
