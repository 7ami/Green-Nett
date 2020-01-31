from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Token, Orders, OrderUpdate,Contact

# Register your models here.


@admin.register(Token, Orders, OrderUpdate,Contact)
class ViewAdmin(ImportExportModelAdmin):
    pass
