from django.contrib import admin
from .import models

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "age",
        "role",
        "email"
    )


admin.site.register(models.User, UserAdmin)
