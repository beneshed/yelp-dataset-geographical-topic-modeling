from django.contrib import admin
from mining.models import Restaurant, Review, Rank, GeoRegion, GeoBusiness

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ['business_id', 'name', 'quadrant', 'latitude', 'longitude', 'stars', 'review_count']
	search_fields = ['business_id', 'name']

class ReviewAdmin(admin.ModelAdmin):
	list_display = ['business_number', 'user_id', 'stars', 'text', 'date']

	def business_number(self, instance):
		return instance.restaurant.business_id

class GeoRegionAdmin(admin.ModelAdmin):
	list_display = ['quadrant', 'x1', 'y1', 'x2', 'y2']

class GeoBusinessAdmin(admin.ModelAdmin):
	list_display = ['business_number', 'level_one']

	def business_number(self, instance):
		return instance.restaurant.business_id

	def level_one(self, instance):
		return instance.level_one.quadrant

admin.site.register(Review, ReviewAdmin)
admin.site.register(Rank)
admin.site.register(GeoRegion, GeoRegionAdmin)
admin.site.register(GeoBusiness, GeoBusinessAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
