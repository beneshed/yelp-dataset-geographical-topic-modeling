# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table(u'mining_restaurant', (
            ('business_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('quadrant', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('full_address', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('stars', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('review_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('categories', self.gf('djorm_pgarray.fields.ArrayField')(default=None, dbtype='varchar(255)', null=True, blank=True)),
            ('open_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'mining', ['Restaurant'])

        # Adding model 'Review'
        db.create_table(u'mining_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mining.Restaurant'], null=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('stars', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('votes', self.gf('djorm_pgarray.fields.ArrayField')(default=None, dbtype='varchar(255)', null=True, blank=True)),
        ))
        db.send_create_signal(u'mining', ['Review'])

        # Adding model 'Rank'
        db.create_table(u'mining_rank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('business_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('effectiveness', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'mining', ['Rank'])

        # Adding model 'GeoRegion'
        db.create_table(u'mining_georegion', (
            ('quadrant', self.gf('django.db.models.fields.IntegerField')(default=0, primary_key=True)),
            ('x1', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('x2', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('y1', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('y2', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'mining', ['GeoRegion'])


    def backwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table(u'mining_restaurant')

        # Deleting model 'Review'
        db.delete_table(u'mining_review')

        # Deleting model 'Rank'
        db.delete_table(u'mining_rank')

        # Deleting model 'GeoRegion'
        db.delete_table(u'mining_georegion')


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