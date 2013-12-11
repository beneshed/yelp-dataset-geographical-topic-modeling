from django.core.management import setup_environ
import settings
setup_environ(settings)
from mining.models import Business, GeoRegion

buses = Business.objects.all()
for bus in buses:
	print bus.latitude	
