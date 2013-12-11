from django.core.management.base import BaseCommand, CommandError
from mining.models import Restaurant, GeoRegion, GeoBusiness

class Command(BaseCommand):

	def handle(self, **options):
		#calculate quad for each object
		rest = Restaurant.objects.all()
		q_one = GeoRegion.objects.get(quadrant=1)
		q_two = GeoRegion.objects.get(quadrant=2)
		q_three = GeoRegion.objects.get(quadrant=3)
		q_four = GeoRegion.objects.get(quadrant=4)
		one = []
		two = []
		three = []
		four = []
		for r in rest:
			x = r.longitude
			y = r.latitude
			up = True
			right = True
			quad = 0
			#check down
			if( y < 33.439857512):
				up = False
			#check left
			if( x < -112.0694951):
				right = False
			if( up == True and right == True):
				print ""#g = GeoBusiness.objects.create(restaurant=r, level_one=q_one, level_two=None, level_three=None, level_four=None) 
				#g.save()
			elif( up == True and right == False):
				print ""#g = GeoBusiness.objects.create(restaurant=r, level_one=q_two, level_two=None, level_three=None, level_four=None) 
				#g.save()
			elif( up == False and right == False):
				print ""#g = GeoBusiness.objects.create(restaurant=r, level_one=q_three, level_two=None, level_three=None, level_four=None) 
				#g.save()
			elif( up == False and right == True):
				g = GeoBusiness.objects.get(restaurant=r)
				g.level_one = q_four
				#g = GeoBusiness.objects.create(restaurant=r, level_one=q_four, level_two=None, level_three=None, level_four=None) 
				g.save()
			else:
				print str(x) + " " + str(y) 
			
			
