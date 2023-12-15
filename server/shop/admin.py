from .models import User, Category, Product
from django.contrib import admin
from django.utils.html import mark_safe
from django.db.models import Value
from django.db.models.functions import Concat
from django.contrib.auth.models import Permission
from .actions import *
from .forms import ProductAdminForm

class UserAdmin(admin.ModelAdmin):
    list_editable = ["is_active"]
    date_hierarchy = "date_joined"
    list_display = [
        "id",
        "username",
        "full_name",
        "avatar_url",
        "is_superuser",
        "is_active",
        "date_joined",
    ]
    list_display_links = ["id", "username", "full_name"]
    search_fields = ["username"]
    list_filter = ["is_active", "is_superuser", "is_staff"]
    list_per_page = 20

    @admin.display(description="Full Name")
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".upper()

    @admin.display(
        description="Avatar",
        ordering=Concat("first_name", Value(" "), "last_name"),
        boolean=False,
    )
    def avatar_url(self, obj):
        if obj.avatar:
            return mark_safe(
                '<img src="%s" alt="%s" width="70" height="70" class="img-thumbnail rounded-circle"/>'
                % (obj.avatar.url, obj.username)
            )

        return mark_safe(
            '<p class="font-italic"><strong class="text-danger">Danger!</strong> You should upload avatar.</p>'
        )


class ProductInline(admin.StackedInline):
    model = Product
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_editable = ["is_active"]
    date_hierarchy = "created_at"
    list_display = [
        "id",
        "name",
        "is_active",
        "created_at",
    ]
    list_display_links = [
        "id",
        "name",
    ]
    search_fields = ["name"]
    list_filter = ["is_active"]
    list_per_page = 20

    inlines = [ProductInline]


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    
    list_editable = ["is_active"]
    date_hierarchy = "created_at"
    list_display = [
        "id",
        "name",
        "price",
        "is_active",
        "category",
        "created_at",
    ]
    list_display_links = ["id", "name", "category"]
    search_fields = ["name", "category__name"]
    list_filter = ["is_active", "category__name"]
    list_per_page = 20


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Permission)
admin.site.add_action(make_actived, "Make Disactived")
admin.site.add_action(export_as_json, "Export as JSON")
admin.site.add_action(export_as_csv, "Export as CSV")

admin.site.site_title = "E-Shop Administrator"
admin.site.site_header = "E-Shop Administrator"
admin.site.index_title = "Welcome To E-Shop Administrator"
