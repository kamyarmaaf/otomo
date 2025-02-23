from django.contrib import admin
from .models import Review, Khabar, CarSpecs


# Register your models here.


class CarSpecsInline(admin.StackedInline):
    model = CarSpecs


class ReviewAdmin(admin.ModelAdmin):
    inlines = [CarSpecsInline]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "date")


class KhabarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "date")


admin.site.register(Review, ReviewAdmin)
admin.site.register(Khabar, KhabarAdmin)
