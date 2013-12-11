from django.db import models
from djorm_pgarray.fields import ArrayField
from djorm_expressions.models import ExpressionManager
# Create your models here.
class Restaurant(models.Model):
    business_id = models.CharField(primary_key=True, unique=True, max_length=50)
    name = models.CharField(max_length=100)
    quadrant = models.IntegerField(default=0) 
    full_address = models.CharField(max_length=150)
    city =  models.CharField(max_length=25)
    state = models.CharField(max_length=10)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    stars = models.FloatField(default=0.0)
    review_count = models.IntegerField(default=0)
    categories = ArrayField(dbtype="varchar(255)")
    open_status = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.business_id

    class Meta:
        verbose_name_plural = "Restaurants"

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, unique=False, null=True)
    user_id = models.CharField(max_length=50)
    stars = models.FloatField(default=0.0)
    text = models.TextField()
    date = models.DateField()
    votes = ArrayField(dbtype="varchar(255)")

    def __unicode__(self):
        return '%s' % self.restaurant.business_id + " " + self.user_id

class Rank(models.Model):
    rank = models.IntegerField(default=0)
    business_id = models.CharField(max_length=50)
    effectiveness = models.FloatField(default=0.0)

class GeoRegion(models.Model):
    quadrant = models.IntegerField(primary_key=True,default=0)
    x1 = models.FloatField(default=0.0)
    x2 = models.FloatField(default=0.0)
    y1 = models.FloatField(default=0.0)
    y2 = models.FloatField(default=0.0)

    def __unicode__(self):
        return '%s' % self.quadrant

class TopicModels(models.Model):
    region = models.ForeignKey(GeoRegion, unique=False)
    topic = models.CharField(max_length=50)

class GeoBusiness(models.Model):
    restaurant = models.ForeignKey(Restaurant, unique=False)
    level_one = models.ForeignKey(GeoRegion, unique=False, null=True, related_name='geobusiness_lone')
    level_two = models.ForeignKey(GeoRegion, unique=False, null=True, related_name='geobusiness_ltwo')
    level_three = models.ForeignKey(GeoRegion, unique=False, null=True, related_name='geobusiness_lthree')
    level_four = models.ForeignKey(GeoRegion, unique=False, null=True, related_name='geobusiness_lfour')

    def __unicode__(self):
        return '%s' % self.restaurant.business_id
