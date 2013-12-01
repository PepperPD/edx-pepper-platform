# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transaction'
        db.create_table('transaction', (
            ('owner_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True, db_index=True)),
            ('subscription_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('term_months', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('student', ['Transaction'])

        # Adding model 'GradeLevel'
        db.create_table('grade_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('student', ['GradeLevel'])

        # Adding model 'YearsInEducation'
        db.create_table('years_in_education', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('student', ['YearsInEducation'])

        # Adding model 'School'
        db.create_table('school', (
            ('district', self.gf('django.db.models.fields.related.OneToOneField')(related_name='school', unique=True, to=orm['student.District'])),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('district_id', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal('student', ['School'])

        # Adding model 'Cohort'
        db.create_table('cohort', (
            ('district', self.gf('django.db.models.fields.related.OneToOneField')(related_name='cohort', unique=True, to=orm['student.District'])),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True, db_index=True)),
            ('licences', self.gf('django.db.models.fields.IntegerField')()),
            ('term_months', self.gf('django.db.models.fields.IntegerField')()),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('student', ['Cohort'])

        # Adding model 'District'
        db.create_table('district', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('state_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('student', ['District'])

        # Adding model 'SubjectArea'
        db.create_table('subject_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('student', ['SubjectArea'])

        # Adding model 'State'
        db.create_table('state', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('student', ['State'])

        # Adding field 'UserProfile.district'
        db.add_column('auth_userprofile', 'district',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2013, 11, 24, 0, 0), related_name='profile', unique=True, to=orm['student.District']),
                      keep_default=False)

        # Adding field 'UserProfile.cohort'
        db.add_column('auth_userprofile', 'cohort',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2013, 11, 24, 0, 0), related_name='profile', unique=True, to=orm['student.Cohort']),
                      keep_default=False)

        # Adding field 'UserProfile.major_subject_area_id'
        db.add_column('auth_userprofile', 'major_subject_area_id',
                      self.gf('django.db.models.fields.CharField')(db_index=True, default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.grade_level_id'
        db.add_column('auth_userprofile', 'grade_level_id',
                      self.gf('django.db.models.fields.CharField')(db_index=True, default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.school_id'
        db.add_column('auth_userprofile', 'school_id',
                      self.gf('django.db.models.fields.CharField')(db_index=True, default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.years_in_education_id'
        db.add_column('auth_userprofile', 'years_in_education_id',
                      self.gf('django.db.models.fields.CharField')(db_index=True, default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.district_id'
        db.add_column('auth_userprofile', 'district_id',
                      self.gf('django.db.models.fields.CharField')(db_index=True, default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.cohort_id'
        db.add_column('auth_userprofile', 'cohort_id',
                      self.gf('django.db.models.fields.CharField')(db_index=True, default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.first_name'
        db.add_column('auth_userprofile', 'first_name',
                      self.gf('django.db.models.fields.CharField')(db_index=True, default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.last_name'
        db.add_column('auth_userprofile', 'last_name',
                      self.gf('django.db.models.fields.CharField')(db_index=True, default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.bio'
        db.add_column('auth_userprofile', 'bio',
                      self.gf('django.db.models.fields.CharField')(db_index=True, default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.subscription_status'
        db.add_column('auth_userprofile', 'subscription_status',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 11, 24, 0, 0), max_length=20),
                      keep_default=False)

        # Adding field 'UserProfile.subscription_start_date'
        db.add_column('auth_userprofile', 'subscription_start_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 24, 0, 0)),
                      keep_default=False)

        # Adding field 'PendingNameChange.new_first_name'
        db.add_column('student_pendingnamechange', 'new_first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'PendingNameChange.new_last_name'
        db.add_column('student_pendingnamechange', 'new_last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Transaction'
        db.delete_table('transaction')

        # Deleting model 'GradeLevel'
        db.delete_table('grade_level')

        # Deleting model 'YearsInEducation'
        db.delete_table('years_in_education')

        # Deleting model 'School'
        db.delete_table('school')

        # Deleting model 'Cohort'
        db.delete_table('cohort')

        # Deleting model 'District'
        db.delete_table('district')

        # Deleting model 'SubjectArea'
        db.delete_table('subject_area')

        # Deleting model 'State'
        db.delete_table('state')

        # Deleting field 'UserProfile.district'
        db.delete_column('auth_userprofile', 'district_id')

        # Deleting field 'UserProfile.cohort'
        db.delete_column('auth_userprofile', 'cohort_id')

        # Deleting field 'UserProfile.major_subject_area_id'
        db.delete_column('auth_userprofile', 'major_subject_area_id')

        # Deleting field 'UserProfile.grade_level_id'
        db.delete_column('auth_userprofile', 'grade_level_id')

        # Deleting field 'UserProfile.school_id'
        db.delete_column('auth_userprofile', 'school_id')

        # Deleting field 'UserProfile.years_in_education_id'
        db.delete_column('auth_userprofile', 'years_in_education_id')

        # Deleting field 'UserProfile.district_id'
        db.delete_column('auth_userprofile', 'district_id')

        # Deleting field 'UserProfile.cohort_id'
        db.delete_column('auth_userprofile', 'cohort_id')

        # Deleting field 'UserProfile.first_name'
        db.delete_column('auth_userprofile', 'first_name')

        # Deleting field 'UserProfile.last_name'
        db.delete_column('auth_userprofile', 'last_name')

        # Deleting field 'UserProfile.bio'
        db.delete_column('auth_userprofile', 'bio')

        # Deleting field 'UserProfile.subscription_status'
        db.delete_column('auth_userprofile', 'subscription_status')

        # Deleting field 'UserProfile.subscription_start_date'
        db.delete_column('auth_userprofile', 'subscription_start_date')

        # Deleting field 'PendingNameChange.new_first_name'
        db.delete_column('student_pendingnamechange', 'new_first_name')

        # Deleting field 'PendingNameChange.new_last_name'
        db.delete_column('student_pendingnamechange', 'new_last_name')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'student.cohort': {
            'Meta': {'object_name': 'Cohort', 'db_table': "'cohort'"},
            'district': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'cohort'", 'unique': 'True', 'to': "orm['student.District']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True', 'db_index': 'True'}),
            'licences': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'term_months': ('django.db.models.fields.IntegerField', [], {})
        },
        'student.courseenrollment': {
            'Meta': {'ordering': "('user', 'course_id')", 'unique_together': "(('user', 'course_id'),)", 'object_name': 'CourseEnrollment'},
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "'honor'", 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'student.courseenrollmentallowed': {
            'Meta': {'unique_together': "(('email', 'course_id'),)", 'object_name': 'CourseEnrollmentAllowed'},
            'auto_enroll': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'student.district': {
            'Meta': {'object_name': 'District', 'db_table': "'district'"},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'state_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'student.gradelevel': {
            'Meta': {'object_name': 'GradeLevel', 'db_table': "'grade_level'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'student.pendingemailchange': {
            'Meta': {'object_name': 'PendingEmailChange'},
            'activation_key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_email': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'student.pendingnamechange': {
            'Meta': {'object_name': 'PendingNameChange'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'new_last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'new_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rationale': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'student.registration': {
            'Meta': {'object_name': 'Registration', 'db_table': "'auth_registration'"},
            'activation_key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'student.school': {
            'Meta': {'object_name': 'School', 'db_table': "'school'"},
            'district': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'school'", 'unique': 'True', 'to': "orm['student.District']"}),
            'district_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'student.state': {
            'Meta': {'object_name': 'State', 'db_table': "'state'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'student.subjectarea': {
            'Meta': {'object_name': 'SubjectArea', 'db_table': "'subject_area'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'student.testcenterregistration': {
            'Meta': {'object_name': 'TestCenterRegistration'},
            'accommodation_code': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'accommodation_request': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'authorization_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'client_authorization_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'confirmed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'eligibility_appointment_date_first': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'eligibility_appointment_date_last': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'exam_series_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'testcenter_user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['student.TestCenterUser']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'upload_error_message': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'upload_status': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '20', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'user_updated_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        },
        'student.testcenteruser': {
            'Meta': {'object_name': 'TestCenterUser'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'address_3': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'candidate_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'client_candidate_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'confirmed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'extension': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '8', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'fax_country_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'phone_country_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_index': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '16', 'blank': 'True'}),
            'processed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'salutation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '20', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'upload_error_message': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'upload_status': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '20', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'unique': 'True'}),
            'user_updated_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        },
        'student.transaction': {
            'Meta': {'object_name': 'Transaction', 'db_table': "'transaction'"},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True', 'db_index': 'True'}),
            'owner_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'subscription_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'term_months': ('django.db.models.fields.IntegerField', [], {})
        },
        'student.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "'auth_userprofile'"},
            'allow_certificate': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'bio': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'cohort': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['student.Cohort']"}),
            'cohort_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'courseware': ('django.db.models.fields.CharField', [], {'default': "'course.xml'", 'max_length': '255', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['student.District']"}),
            'district_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'goals': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'grade_level_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'level_of_education': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'mailing_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'major_subject_area_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'meta': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'school_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'subscription_start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'subscription_status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'year_of_birth': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'years_in_education_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'})
        },
        'student.usertestgroup': {
            'Meta': {'object_name': 'UserTestGroup'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'db_index': 'True', 'symmetrical': 'False'})
        },
        'student.yearsineducation': {
            'Meta': {'object_name': 'YearsInEducation', 'db_table': "'years_in_education'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['student']