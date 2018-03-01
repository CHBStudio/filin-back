from django.contrib import admin

from app.models import ProductService, Company, Lease


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'description', 'phone', 'floor', 'housing', 'get_tags')
    fields = ('name', 'link', 'description', 'phone', 'floor', 'housing', 'tags')
    list_filter = ('floor',)

    def get_tags(self, obj):
        return ', '.join([_.title for _ in obj.tags.all()])

    get_tags.short_description = 'Услуги и товары'


class LeaseAdmin(admin.ModelAdmin):
    list_display = ('photo', 'square', 'cost', 'floor', 'housing', 'function', 'show', 'order')
    fields = ('photo', 'square', 'cost', 'floor', 'housing', 'function', 'show', 'order')
    list_filter = ('floor', 'cost')


class ProductServiceAdmin(admin.ModelAdmin):
    list_display = ('title','type')
    fields = ('title', 'type')
    list_filter = ('type',)


admin.site.register(ProductService, ProductServiceAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Lease, LeaseAdmin)
