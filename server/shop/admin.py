import csv
from .models import User
from django.contrib import admin, messages
from django.utils.html import mark_safe
from django.db.models import Value
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import Permission
from django.utils.translation import ngettext


@admin.action(description="Mark selected models as disactived")
def make_actived(self, request, queryset):
    updated = queryset.update(is_active=False)
    self.message_user(
        request,
        ngettext(
            "%d model was successfully marked as disactived.",
            "%d models were successfully marked as disactived.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


@admin.action(description="Mark selected models as export file JSON")
def export_as_json(self, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response


@admin.action(description="Mark selected models as export file CSV")
def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response


class UserAdmin(admin.ModelAdmin):
    list_editable = ["is_active"]
    date_hierarchy = "date_joined"
    list_display = ["id", "username", "full_name", "avatar_url", "is_superuser", "is_active", "date_joined"]
    list_display_links = ["id", "username", "full_name"]
    search_fields = ["username"]
    list_filter = ["is_active", "is_superuser", "is_staff"]
    list_per_page = 20
    
    @admin.display(description="Full Name")
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".upper()

    @admin.display(description="Avatar", ordering=Concat("first_name", Value(" "), "last_name"), boolean=False)
    def avatar_url(self, obj):
        if obj.avatar:
            return mark_safe(
                '<img src="%s" alt="%s" width="70" height="70" class="img-thumbnail rounded-circle"/>' % (obj.avatar.url, obj.username)
            )

        return mark_safe(
            '<p class="font-italic"><strong class="text-danger">Danger!</strong> You should upload avatar.</p>'
        )

admin.site.register(User, UserAdmin)
admin.site.add_action(make_actived, "Make Disactived")
admin.site.add_action(export_as_json, "Export as JSON")
admin.site.add_action(export_as_csv, "Export as CSV")

admin.site.site_title = 'E-Shop Administrator'
admin.site.site_header = 'E-Shop Administrator'
admin.site.index_title = 'Welcome To E-Shop Administrator'