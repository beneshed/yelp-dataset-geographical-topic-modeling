from django.core.management.base import BaseCommand, CommandError
from mining.models import Business, GeoRegion

class Command(BaseCommand):

	def handle(self, **options):
		#calculate quad for each object
		buses = Business.objects.all()
		quad1 = GeoRegion.objects.get(quadrant=1)
		quad2 = GeoRegion.objects.get(quadrant=2)
		quad3 = GeoRegion.objects.get(quadrant=3)
		quad4 = GeoRegion.objects.get(quadrant=4)
		for bus in buses:
			x = bus.longitude
			y = bus.latitude
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
				quad = 1
			elif( up == True and right == False):
				quad = 2
			elif( up == False and right == False):
				quad = 3
			elif( up == False and right == True):
				quad = 4
			else:
				print str(x) + " " + str(y) 
			bus.quadrant = quad
			bus.save()
