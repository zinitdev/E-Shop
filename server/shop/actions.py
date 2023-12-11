import csv
from django.contrib import admin, messages
from django.http import HttpResponse
from django.core import serializers
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
