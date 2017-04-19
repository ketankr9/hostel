# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Limbdi2016(models.Model):
    room = models.IntegerField(blank=True, null=True)
    list_display = ('room')
    class Meta:
        managed = False
        db_table = 'limbdi2016'
    def __str__(self):
        return str(self.room)


class LimbdiHostel(models.Model):
    room_no = models.IntegerField(primary_key=True)
    a = models.CharField(db_column='A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'limbdi_hostel'


class LimbdiMessOdd(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    jan = models.CharField(max_length=10, blank=True, null=True)
    feb = models.CharField(max_length=10, blank=True, null=True)
    mar = models.CharField(max_length=10, blank=True, null=True)
    apr = models.CharField(max_length=10, blank=True, null=True)
    may = models.CharField(max_length=10, blank=True, null=True)
    jun = models.CharField(max_length=10, blank=True, null=True)
    jul = models.CharField(max_length=10, blank=True, null=True)
    aug = models.CharField(max_length=10, blank=True, null=True)
    sep = models.CharField(max_length=10, blank=True, null=True)
    oct = models.CharField(max_length=10, blank=True, null=True)
    nov = models.CharField(max_length=10, blank=True, null=True)
    dece = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limbdi_mess_odd'


class Profile(models.Model):
    course_choices=(
    ('IMD','Integrated Masters Degree'),
    ('IDD','Integrated Dual Degree'),
    ('B.Tech','Bachlors of Technology'),
    ('PhD','Doctors Degree'),
    ('None','None of the above'),
    )
    branch_choices=(
    ('cse','Computer Science and Engineering'),
    ('mnc','Mathematics and Computing'),
    ('ece','Electrical and Communication Engineering'),
    ('cer','Ceramic Engineering'),
    ('None','None of the above'),
    )
    room_sec_choices=(
    ('a','A'),
    ('b','B'),
    ('c','C'),
    )
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    # branch = models.CharField(max_length=20, blank=True, null=True)
    branch = models.CharField(max_length=5, choices=branch_choices)
    acad_fee = models.CharField(max_length=50, blank=True, null=True)
    mess_fee = models.CharField(max_length=50, blank=True, null=True)
    room_sec = models.CharField(max_length=10,choices = room_sec_choices ,blank=True, null=True)
    room_no = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    # course = models.CharField(max_length=20, blank=True, null=True)
    course = models.CharField(max_length=9, choices=course_choices)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)

    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)
    #pic = models.FileField(upload_to="/home/uk/django/hostel/")
    class Meta:
        managed = False
        #order_with_respect_to = 'roll_no'
        db_table = 'profile'
        ordering=('roll_no',)
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name





class Aryabhatta(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aryabhatta'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name


class Cvraman(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cvraman'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name


class Dhanrajgiri(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dhanrajgiri'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name


class Gmscnew(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmscnew'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name

class Gmscold(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmscold'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name

class Limbdi(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limbdi'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name


class Morvi(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'morvi'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name

class Rajputana(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rajputana'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name


class Ramanujan(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ramanujan'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name


class Saluja(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saluja'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name


class Scdey(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scdey'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name


class Snbose(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snbose'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name


class Vishwakarma(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vishwakarma'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name


class Vishweshvarayya(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vishweshvarayya'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name


class Vivekananda(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    acad_fee = models.CharField(max_length=255, blank=True, null=True)
    mess_fee = models.CharField(max_length=255, blank=True, null=True)
    room_sec = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    passing_year = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    bank_acount_no = models.CharField(max_length=20, blank=True, null=True)
    ifs_code = models.CharField(max_length=20, blank=True, null=True)
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_phone = models.CharField(max_length=20, blank=True, null=True)
    guardian_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vivekananda'
    def __str__(self):
        return ""+str(self.roll_no)+" "+self.name
