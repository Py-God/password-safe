from django.contrib import admin
from .models import Site, Account


class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("siteName",)}


class AccountAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_field": ("username",)}


admin.site.register(Site, SiteAdmin)
admin.site.register(Account, AccountAdmin)
