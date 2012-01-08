# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'FeedBack.contact_number'
        db.delete_column('feedback_feedback', 'contact_number')

        # Deleting field 'FeedBack.name'
        db.delete_column('feedback_feedback', 'name')

        # Deleting field 'FeedBack.type'
        db.delete_column('feedback_feedback', 'type')

        # Deleting field 'FeedBack.email'
        db.delete_column('feedback_feedback', 'email')

        # Adding field 'FeedBack.feedback_name'
        db.add_column('feedback_feedback', 'feedback_name', self.gf('django.db.models.fields.CharField')(default=1, max_length=25), keep_default=False)

        # Adding field 'FeedBack.feedback_email'
        db.add_column('feedback_feedback', 'feedback_email', self.gf('django.db.models.fields.EmailField')(default=1, max_length=75), keep_default=False)

        # Adding field 'FeedBack.feedback_contact_number'
        db.add_column('feedback_feedback', 'feedback_contact_number', self.gf('django.db.models.fields.CharField')(default=1, max_length=15), keep_default=False)

        # Adding field 'FeedBack.feedback_type'
        db.add_column('feedback_feedback', 'feedback_type', self.gf('django.db.models.fields.CharField')(default='suggestion', max_length=25), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'FeedBack.contact_number'
        db.add_column('feedback_feedback', 'contact_number', self.gf('django.db.models.fields.CharField')(default=1, max_length=15), keep_default=False)

        # Adding field 'FeedBack.name'
        db.add_column('feedback_feedback', 'name', self.gf('django.db.models.fields.CharField')(default=1, max_length=25), keep_default=False)

        # Adding field 'FeedBack.type'
        db.add_column('feedback_feedback', 'type', self.gf('django.db.models.fields.CharField')(default=1, max_length=25), keep_default=False)

        # Adding field 'FeedBack.email'
        db.add_column('feedback_feedback', 'email', self.gf('django.db.models.fields.EmailField')(default=1, max_length=75), keep_default=False)

        # Deleting field 'FeedBack.feedback_name'
        db.delete_column('feedback_feedback', 'feedback_name')

        # Deleting field 'FeedBack.feedback_email'
        db.delete_column('feedback_feedback', 'feedback_email')

        # Deleting field 'FeedBack.feedback_contact_number'
        db.delete_column('feedback_feedback', 'feedback_contact_number')

        # Deleting field 'FeedBack.feedback_type'
        db.delete_column('feedback_feedback', 'feedback_type')


    models = {
        'feedback.feedback': {
            'Meta': {'ordering': "('-post_date',)", 'object_name': 'FeedBack'},
            'feedback': ('django.db.models.fields.TextField', [], {}),
            'feedback_contact_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'feedback_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'feedback_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'feedback_type': ('django.db.models.fields.CharField', [], {'default': "'suggestion'", 'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['feedback']
