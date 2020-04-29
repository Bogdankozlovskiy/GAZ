from django.contrib import admin
from .models import Curator, CustomUser, FinanceCosts, Quart, CuratorQuartCosts, Contract


admin.site.register(Curator)
admin.site.register(FinanceCosts)
admin.site.register(CustomUser)
@admin.register(Quart)
class QuartAdmin(admin.ModelAdmin):
    list_display =('title', 'finance_cost', 'total')
    ordering = ('title', 'finance_cost')
    list_filter = ('finance_cost',)

admin.site.register(Contract)



@admin.register(CuratorQuartCosts)
class CuratorQuartCostsAdmin(admin.ModelAdmin):
    list_display = ('quart', 'curator', 'total')
    ordering = ('quart', 'curator')
    list_filter =('quart', 'curator')

# Register your models here.
