from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from .serializers import (
    GroupSerializer,
    UserSerializer,
    CategorySerializer,
    ProductSerializer,
)
from . import dao


class UserViewSet(viewsets.ModelViewSet):
    queryset = dao.load_users()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get_permissions(self):
    #     if self.action == "create":
    #         permission_classes = [permissions.AllowAny]
    #     else:
    #         permission_classes = [permissions.IsAuthenticated]
        
    #     return [permission() for permission in permission_classes]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = dao.load_groups()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = dao.load_categories()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = dao.load_products()
    serializer_class = ProductSerializer
