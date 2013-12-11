# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
	from django.core.management import call_command
        call_command("loaddata", "active_restaurant_reviews1.json")


    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'mining.georegion': {
            'Meta': {'object_name': 'GeoRegion'},
            'quadrant': ('django.db.models.fields.IntegerField', [], {'default': '0', 'primary_key': 'True'}),
            'x1': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'x2': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'y1': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'y2': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        u'mining.rank': {
            'Meta': {'object_name': 'Rank'},
            'business_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'effectiveness': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'mining.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'business_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'}),
            'categories': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'varchar(255)'", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'full_address': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'open_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quadrant': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'review_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stars': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'mining.review': {
            'Meta': {'object_name': 'Review'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mining.Restaurant']", 'null': 'True'}),
            'stars': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'votes': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'varchar(255)'", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mining']
    symmetrical = True
