from django.contrib import admin
from agency.models import SpyCat, Mission, Target


class TargetInline(admin.TabularInline):
    model = Target
    extra = 1


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    inlines = [TargetInline]


admin.site.register(SpyCat)
