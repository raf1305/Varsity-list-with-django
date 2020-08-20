from django.contrib import admin
from .models import Varsity
# Register your models here.
# admin.site.register(Varsity)

@admin.register(Varsity)
class VarsityAdmin(admin.ModelAdmin):
    list_display=('univarsity_name','univarsity_nickname','location','category')
    list_filter = ('specailization','category')

    fieldsets = (
        ('Name', {
            'fields': ('univarsity_name', 'univarsity_nickname')
        }),
        ('Location', {
            'fields': ('location', 'division')
        }),
        ('Speciality', {
            'fields': ('specailization', 'category','phdgranting')
        }),
        ('Additional', {
            'fields': ('foundation', 'link')
        }),

    )