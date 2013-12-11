from django.core.management.base import BaseCommand, CommandError
from mining.models import Restaurant, GeoRegion, GeoBusiness, Review

class Command(BaseCommand):

	def handle(self, **options):
		#calculate quad for each object
		#quad one reviews
		file_one_name = 'quadrant_three.txt'
		f = open(file_one_name, 'a' )
		level_one_rests = GeoBusiness.objects.filter(level_one=3)
		for one in level_one_rests:
			rest_id = one.restaurant.business_id
			rest_reviews = Review.objects.filter(restaurant__business_id = rest_id)
			for revs in rest_reviews:
			    text_out = revs.text
                            text_out = text_out.encode('utf-8')
			    f.write(text_out)
		f.close()
			    #with open(file_one_name, "a", "utf-8") as myfile:
			#	print revs.text
    			#	myfile.write(str(revs.text))
		#quad two objects
		#file_two_name = 'quadrant_two.txt'
		#rest_two = GeoBusiness.objects.filter(level_one=2)
		#quad three objects
		#file_three_name = 'quadrant_three.txt'
		#rest_three = GeoBusiness.objects.filter(level_one=3)
		#quad four objects
		#file_four_name = 'quadrant_four.txt'
			
