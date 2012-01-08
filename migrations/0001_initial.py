# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FeedBack'
        db.create_table('feedback_feedback', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('contact_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('feedback', self.gf('django.db.models.fields.TextField')()),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('feedback', ['FeedBack'])


    def backwards(self, orm):
        
        # Deleting model 'FeedBack'
        db.delete_table('feedback_feedback')


    models = {
        'feedback.feedback': {
            'Meta': {'ordering': "('-post_date',)", 'object_name': 'FeedBack'},
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'feedback': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['feedback']
