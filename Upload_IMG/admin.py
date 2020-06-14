from django.contrib import admin
from Upload_IMG.models import   Upload_IMG


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',  'image')  # list
    search_fields = ('name',)
    # inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'image'),
        }],
    )

admin.site.register(Upload_IMG, ContactAdmin)
admin.site.site_header = 'Images-Manager'
admin.site.site_title = 'Login'
admin.site.index_title = 'Images-Manager'
