from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer, CategorySerializer, ProductSerializer
from . import dao
from rest_framework import generics


class UserViewSet(viewsets.ModelViewSet):
    queryset = dao.load_users()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


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
