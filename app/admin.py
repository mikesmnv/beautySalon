from django.contrib import admin

from .models import Categories, SubCategories, Services, Team

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Team)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    pass


# Register your models here.
