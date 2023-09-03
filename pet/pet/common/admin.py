from django.contrib import admin
# TODO
from pet.common.models import PhotoComment


@admin.register(PhotoComment)
class CommonAdmin(admin.ModelAdmin):
    pass
