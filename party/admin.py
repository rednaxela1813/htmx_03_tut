from django.contrib import admin
from .models import Party, Gift, Guest, CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ["venue", "party_date", "party_time", "organizer"]
    search_fields = ["venue", "party_date", "party_time", "organizer"]
    readonly_fields = ["uuid"]


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ["gift", "price", "link", "party"]
    search_fields = ["gift", "price", "link", "party"]
    readonly_fields = ["uuid"]


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ["name", "attending", "party"]
    search_fields = ["name", "attending", "party"]
    readonly_fields = ["uuid"]