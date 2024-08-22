from django.contrib import admin

from .models import FormModel, FormField


@admin.register(FormModel)
class FormModelAdmin(admin.ModelAdmin):
    pass


@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    pass
