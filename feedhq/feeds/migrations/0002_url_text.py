# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Feed.url'
        db.alter_column(u'feeds_feed', 'url', self.gf('feedhq.feeds.fields.URLField')())

        # Changing field 'Favicon.url'
        db.alter_column(u'feeds_favicon', 'url', self.gf('feedhq.feeds.fields.URLField')(unique=True))

        # Changing field 'Entry.permalink'
        db.alter_column(u'feeds_entry', 'permalink', self.gf('feedhq.feeds.fields.URLField')())

        # Changing field 'Entry.link'
        db.alter_column(u'feeds_entry', 'link', self.gf('feedhq.feeds.fields.URLField')())

        # Changing field 'Entry.read_later_url'
        db.alter_column(u'feeds_entry', 'read_later_url', self.gf('feedhq.feeds.fields.URLField')())

        # Changing field 'UniqueFeed.hub'
        db.alter_column(u'feeds_uniquefeed', 'hub', self.gf('feedhq.feeds.fields.URLField')(null=True))

        # Changing field 'UniqueFeed.url'
        db.alter_column(u'feeds_uniquefeed', 'url', self.gf('feedhq.feeds.fields.URLField')(unique=True))

        # Changing field 'UniqueFeed.link'
        db.alter_column(u'feeds_uniquefeed', 'link', self.gf('feedhq.feeds.fields.URLField')())

    def backwards(self, orm):

        # Changing field 'Feed.url'
        db.alter_column(u'feeds_feed', 'url', self.gf('django.db.models.fields.URLField')(max_length=1023))

        # Changing field 'Favicon.url'
        db.alter_column(u'feeds_favicon', 'url', self.gf('django.db.models.fields.URLField')(max_length=2048, unique=True))

        # Changing field 'Entry.permalink'
        db.alter_column(u'feeds_entry', 'permalink', self.gf('django.db.models.fields.URLField')(max_length=1023))

        # Changing field 'Entry.link'
        db.alter_column(u'feeds_entry', 'link', self.gf('django.db.models.fields.URLField')(max_length=1023))

        # Changing field 'Entry.read_later_url'
        db.alter_column(u'feeds_entry', 'read_later_url', self.gf('django.db.models.fields.URLField')(max_length=1023))

        # Changing field 'UniqueFeed.hub'
        db.alter_column(u'feeds_uniquefeed', 'hub', self.gf('django.db.models.fields.URLField')(max_length=1023, null=True))

        # Changing field 'UniqueFeed.url'
        db.alter_column(u'feeds_uniquefeed', 'url', self.gf('django.db.models.fields.URLField')(max_length=1023, unique=True))

        # Changing field 'UniqueFeed.link'
        db.alter_column(u'feeds_uniquefeed', 'link', self.gf('django.db.models.fields.URLField')(max_length=2048))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'entries_per_page': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'read_later': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'read_later_credentials': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sharing_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sharing_gplus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sharing_twitter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '75'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'feeds.category': {
            'Meta': {'ordering': "('order', 'name', 'id')", 'object_name': 'Category'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'pale-green'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1023'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categories'", 'to': u"orm['auth.User']"})
        },
        u'feeds.entry': {
            'Meta': {'ordering': "('-date', 'title')", 'object_name': 'Entry'},
            'broadcast': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': u"orm['feeds.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('feedhq.feeds.fields.URLField', [], {}),
            'permalink': ('feedhq.feeds.fields.URLField', [], {'blank': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'read_later_url': ('feedhq.feeds.fields.URLField', [], {'blank': 'True'}),
            'starred': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'subtitle': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': u"orm['auth.User']"})
        },
        u'feeds.favicon': {
            'Meta': {'object_name': 'Favicon'},
            'favicon': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('feedhq.feeds.fields.URLField', [], {'unique': 'True', 'db_index': 'True'})
        },
        u'feeds.feed': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Feed'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feeds'", 'to': u"orm['feeds.Category']"}),
            'favicon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_safe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'unread_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'url': ('feedhq.feeds.fields.URLField', [], {})
        },
        u'feeds.uniquefeed': {
            'Meta': {'object_name': 'UniqueFeed'},
            'backoff_factor': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'error': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_column': "'muted_reason'", 'blank': 'True'}),
            'etag': ('django.db.models.fields.CharField', [], {'max_length': '1023', 'null': 'True', 'blank': 'True'}),
            'hub': ('feedhq.feeds.fields.URLField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_loop': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'link': ('feedhq.feeds.fields.URLField', [], {'blank': 'True'}),
            'modified': ('django.db.models.fields.CharField', [], {'max_length': '1023', 'null': 'True', 'blank': 'True'}),
            'muted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'subscribers': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'blank': 'True'}),
            'url': ('feedhq.feeds.fields.URLField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['feeds']