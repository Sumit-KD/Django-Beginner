from django.contrib import admin
from .models import Chaivarity, ChaiReviews, Chai_Certificate, Store

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReviews
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_no')

admin.site.register(Chaivarity, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Chai_Certificate, ChaiCertificateAdmin)
