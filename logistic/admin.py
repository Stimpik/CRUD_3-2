from django.contrib import admin

from logistic.models import StockProduct, Product, Stock


class MeasurementInline(admin.TabularInline):
    model = StockProduct
    extra = 2

@admin.register(Product)
class SensorAdmin(admin.ModelAdmin):
    inlines = [MeasurementInline]


@admin.register(Stock)
class MeasurementAdmin(admin.ModelAdmin):
    pass
@admin.register(StockProduct)
class StockProduct(admin.ModelAdmin):
    pass
