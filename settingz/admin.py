from django.contrib import admin
from .models import Settingz

@admin.register(Settingz)
class SettingzAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'email', 'phone', 'address')
    search_fields = ('site_name', 'email', 'phone')
    list_filter = ('address',)
    ordering = ('site_name',)
    fieldsets = (
        (None, {
            'fields': ('site_name', 'email', 'phone', 'address')
        }),
        ('Social Media Links', {
            'fields': ('facebook', 'telegram', 'instagram', 'linkedin')
        }),
        ('Logo', {
            'fields': ('logo', 'title_logo','long_banner')
        }),
        ('Design Credit', {
            'fields': ('design_by',)
        }),
        ('Gallery De',{
            'fields': ('image','caption')
        }),
    )

    def has_add_permission(self, request):
        # Optional: Allow only one instance of Settingz
        return not Settingz.objects.exists()

