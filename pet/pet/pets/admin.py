from django.contrib import admin
from pet.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

