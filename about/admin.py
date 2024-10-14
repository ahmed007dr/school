from django.contrib import admin
from .models import AboutUs

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'video_url')
    search_fields = ('title', 'subtitle', 'description')
    ordering = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'description', 'video_url')
        }),
        ('Features', {
            'fields': ('feature1', 'feature2', 'feature3', 'feature4', 'feature5', 'feature6')
        }),
        ('Links', {
            'fields': ('more_details_link',)
        }),
    )

    def has_add_permission(self, request):
        # Optional: Allow only one instance of AboutUs
        return not AboutUs.objects.exists()

