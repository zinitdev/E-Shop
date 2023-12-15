from django import forms
from .models import Product
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Product
        fields = "__all__"
