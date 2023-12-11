from .models import User, Product, Category
from django.contrib.auth.models import Group


def load_users():
    return User.objects.filter(is_active=True).all().order_by("-date_joined")


def load_groups():
    return Group.objects.all()


def load_categories():
    return Category.objects.filter(is_active=True).all().order_by("-created_at")


def load_products():
    return Product.objects.filter(is_active=True).all().order_by("-created_at")
