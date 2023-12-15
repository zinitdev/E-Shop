from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="uploads/%Y/%m/%d",
        default=None,
        null=True,
        blank=True,
        help_text="Upload avatar of the user.",
    )

    def __str__(self):
        return self.username


class CommonModel(models.Model):
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="Designates whether this model should be treated as active. Unselect this instead of deleting models.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(CommonModel):
    name = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name", "-created_at")

    def __str__(self):
        return self.name


class Product(CommonModel):
    name = models.CharField(max_length=100)
    description = RichTextField(
        null=True,
        blank=True,
        help_text="Description about the product.",
        config_name='default', 
    )
    price = models.FloatField(default=0.00, help_text="Price for this product.")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        help_text="The category this product belongs to.",
    )

    class Meta:
        ordering = ("name", "price", "-created_at", "category")

    def __str__(self):
        return self.name
