# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GeoBusiness'
        db.create_table(u'mining_geobusiness', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mining.Restaurant'])),
            ('level_one', self.gf('django.db.models.fields.related.ForeignKey')(related_name='geobusiness_lone', null=True, to=orm['mining.GeoRegion'])),
            ('level_two', self.gf('django.db.models.fields.related.ForeignKey')(related_name='geobusiness_ltwo', null=True, to=orm['mining.GeoRegion'])),
            ('level_three', self.gf('django.db.models.fields.related.ForeignKey')(related_name='geobusiness_lthree', null=True, to=orm['mining.GeoRegion'])),
            ('level_four', self.gf('django.db.models.fields.related.ForeignKey')(related_name='geobusiness_lfour', null=True, to=orm['mining.GeoRegion'])),
        ))
        db.send_create_signal(u'mining', ['GeoBusiness'])


    def backwards(self, orm):
        # Deleting model 'GeoBusiness'
        db.delete_table(u'mining_geobusiness')


    models = {
        u'mining.geobusiness': {
            'Meta': {'object_name': 'GeoBusiness'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_four': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'geobusiness_lfour'", 'null': 'True', 'to': u"orm['mining.GeoRegion']"}),
            'level_one': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'geobusiness_lone'", 'null': 'True', 'to': u"orm['mining.GeoRegion']"}),
            'level_three': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'geobusiness_lthree'", 'null': 'True', 'to': u"orm['mining.GeoRegion']"}),
            'level_two': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'geobusiness_ltwo'", 'null': 'True', 'to': u"orm['mining.GeoRegion']"}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mining.Restaurant']"})
        },
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