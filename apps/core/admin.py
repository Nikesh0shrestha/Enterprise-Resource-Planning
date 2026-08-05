from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
    )


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company",
        "phone",
    )

    list_filter = ("company",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "branch",
    )

    list_filter = (
        "branch",
    )
