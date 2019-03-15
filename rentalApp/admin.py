from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Property, RentalUnit, Tenant


class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'property_name',
        'property_location',
        'property_type',
 
    )
    list_filter = ('property_name',)
    search_fields = ('property_name',)
admin.site.register(Property, PropertyAdmin)


class RentalUnitAdmin(admin.ModelAdmin):
	list_display = (
		'id',
        'unit_name',
		'unit_description',
		'unit_type',
		'monthly_rent',
		'is_occupied'
		
	)
	list_filter = ('unit_type',)
	search_fields = ('unit_type', 'unit_name')
admin.site.register(RentalUnit, RentalUnitAdmin)


class TenantAdmin(admin.ModelAdmin):
	list_display = (
        'id',
        'user',
		'rental_unit',
        'phone_number',
		'national_id',
		'as_from',
		'until',
		'profile_photo'
		
		
	)
	list_filter = ('user', 'as_from', 'until')
	search_fields = ('user',)
admin.site.register(Tenant, TenantAdmin)


