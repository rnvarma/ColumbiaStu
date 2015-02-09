# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserData'
        db.create_table(u'backend_userdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'backend', ['UserData'])

        # Adding model 'CommentModel'
        db.create_table(u'backend_commentmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'backend', ['CommentModel'])

        # Adding model 'ClassTagModel'
        db.create_table(u'backend_classtagmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
        ))
        db.send_create_signal(u'backend', ['ClassTagModel'])

        # Adding model 'SchoolTagModel'
        db.create_table(u'backend_schooltagmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
        ))
        db.send_create_signal(u'backend', ['SchoolTagModel'])

        # Adding model 'AreaTagModel'
        db.create_table(u'backend_areatagmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
        ))
        db.send_create_signal(u'backend', ['AreaTagModel'])

        # Adding model 'PostModel'
        db.create_table(u'backend_postmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('date_submitted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'backend', ['PostModel'])

        # Adding M2M table for field comments on 'PostModel'
        m2m_table_name = db.shorten_name(u'backend_postmodel_comments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('postmodel', models.ForeignKey(orm[u'backend.postmodel'], null=False)),
            ('commentmodel', models.ForeignKey(orm[u'backend.commentmodel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['postmodel_id', 'commentmodel_id'])

        # Adding M2M table for field classTags on 'PostModel'
        m2m_table_name = db.shorten_name(u'backend_postmodel_classTags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('postmodel', models.ForeignKey(orm[u'backend.postmodel'], null=False)),
            ('classtagmodel', models.ForeignKey(orm[u'backend.classtagmodel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['postmodel_id', 'classtagmodel_id'])

        # Adding M2M table for field schoolTags on 'PostModel'
        m2m_table_name = db.shorten_name(u'backend_postmodel_schoolTags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('postmodel', models.ForeignKey(orm[u'backend.postmodel'], null=False)),
            ('schooltagmodel', models.ForeignKey(orm[u'backend.schooltagmodel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['postmodel_id', 'schooltagmodel_id'])

        # Adding M2M table for field areaTags on 'PostModel'
        m2m_table_name = db.shorten_name(u'backend_postmodel_areaTags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('postmodel', models.ForeignKey(orm[u'backend.postmodel'], null=False)),
            ('areatagmodel', models.ForeignKey(orm[u'backend.areatagmodel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['postmodel_id', 'areatagmodel_id'])

        # Adding M2M table for field author on 'PostModel'
        m2m_table_name = db.shorten_name(u'backend_postmodel_author')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('postmodel', models.ForeignKey(orm[u'backend.postmodel'], null=False)),
            ('userdata', models.ForeignKey(orm[u'backend.userdata'], null=False))
        ))
        db.create_unique(m2m_table_name, ['postmodel_id', 'userdata_id'])

        # Adding model 'LikeModel'
        db.create_table(u'backend_likemodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_submitted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'backend', ['LikeModel'])

        # Adding M2M table for field author on 'LikeModel'
        m2m_table_name = db.shorten_name(u'backend_likemodel_author')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('likemodel', models.ForeignKey(orm[u'backend.likemodel'], null=False)),
            ('userdata', models.ForeignKey(orm[u'backend.userdata'], null=False))
        ))
        db.create_unique(m2m_table_name, ['likemodel_id', 'userdata_id'])

        # Adding M2M table for field post on 'LikeModel'
        m2m_table_name = db.shorten_name(u'backend_likemodel_post')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('likemodel', models.ForeignKey(orm[u'backend.likemodel'], null=False)),
            ('postmodel', models.ForeignKey(orm[u'backend.postmodel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['likemodel_id', 'postmodel_id'])

        # Adding model 'DislikeModel'
        db.create_table(u'backend_dislikemodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_submitted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'backend', ['DislikeModel'])

        # Adding M2M table for field author on 'DislikeModel'
        m2m_table_name = db.shorten_name(u'backend_dislikemodel_author')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dislikemodel', models.ForeignKey(orm[u'backend.dislikemodel'], null=False)),
            ('userdata', models.ForeignKey(orm[u'backend.userdata'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dislikemodel_id', 'userdata_id'])

        # Adding M2M table for field post on 'DislikeModel'
        m2m_table_name = db.shorten_name(u'backend_dislikemodel_post')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dislikemodel', models.ForeignKey(orm[u'backend.dislikemodel'], null=False)),
            ('postmodel', models.ForeignKey(orm[u'backend.postmodel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dislikemodel_id', 'postmodel_id'])


    def backwards(self, orm):
        # Deleting model 'UserData'
        db.delete_table(u'backend_userdata')

        # Deleting model 'CommentModel'
        db.delete_table(u'backend_commentmodel')

        # Deleting model 'ClassTagModel'
        db.delete_table(u'backend_classtagmodel')

        # Deleting model 'SchoolTagModel'
        db.delete_table(u'backend_schooltagmodel')

        # Deleting model 'AreaTagModel'
        db.delete_table(u'backend_areatagmodel')

        # Deleting model 'PostModel'
        db.delete_table(u'backend_postmodel')

        # Removing M2M table for field comments on 'PostModel'
        db.delete_table(db.shorten_name(u'backend_postmodel_comments'))

        # Removing M2M table for field classTags on 'PostModel'
        db.delete_table(db.shorten_name(u'backend_postmodel_classTags'))

        # Removing M2M table for field schoolTags on 'PostModel'
        db.delete_table(db.shorten_name(u'backend_postmodel_schoolTags'))

        # Removing M2M table for field areaTags on 'PostModel'
        db.delete_table(db.shorten_name(u'backend_postmodel_areaTags'))

        # Removing M2M table for field author on 'PostModel'
        db.delete_table(db.shorten_name(u'backend_postmodel_author'))

        # Deleting model 'LikeModel'
        db.delete_table(u'backend_likemodel')

        # Removing M2M table for field author on 'LikeModel'
        db.delete_table(db.shorten_name(u'backend_likemodel_author'))

        # Removing M2M table for field post on 'LikeModel'
        db.delete_table(db.shorten_name(u'backend_likemodel_post'))

        # Deleting model 'DislikeModel'
        db.delete_table(u'backend_dislikemodel')

        # Removing M2M table for field author on 'DislikeModel'
        db.delete_table(db.shorten_name(u'backend_dislikemodel_author'))

        # Removing M2M table for field post on 'DislikeModel'
        db.delete_table(db.shorten_name(u'backend_dislikemodel_post'))


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
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'backend.areatagmodel': {
            'Meta': {'object_name': 'AreaTagModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'})
        },
        u'backend.classtagmodel': {
            'Meta': {'object_name': 'ClassTagModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'})
        },
        u'backend.commentmodel': {
            'Meta': {'object_name': 'CommentModel'},
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'backend.dislikemodel': {
            'Meta': {'object_name': 'DislikeModel'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dislikes'", 'symmetrical': 'False', 'to': u"orm['backend.UserData']"}),
            'date_submitted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dislikes'", 'symmetrical': 'False', 'to': u"orm['backend.PostModel']"})
        },
        u'backend.likemodel': {
            'Meta': {'object_name': 'LikeModel'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'likes'", 'symmetrical': 'False', 'to': u"orm['backend.UserData']"}),
            'date_submitted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'likes'", 'symmetrical': 'False', 'to': u"orm['backend.PostModel']"})
        },
        u'backend.postmodel': {
            'Meta': {'object_name': 'PostModel'},
            'areaTags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'posts'", 'symmetrical': 'False', 'to': u"orm['backend.AreaTagModel']"}),
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'posts'", 'symmetrical': 'False', 'to': u"orm['backend.UserData']"}),
            'classTags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'posts'", 'symmetrical': 'False', 'to': u"orm['backend.ClassTagModel']"}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'post'", 'symmetrical': 'False', 'to': u"orm['backend.CommentModel']"}),
            'date_submitted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'schoolTags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'posts'", 'symmetrical': 'False', 'to': u"orm['backend.SchoolTagModel']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        u'backend.schooltagmodel': {
            'Meta': {'object_name': 'SchoolTagModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'})
        },
        u'backend.userdata': {
            'Meta': {'object_name': 'UserData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['backend']