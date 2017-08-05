from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from lhsauth.models import User


class Alias(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    type = models.IntegerField()

    class Meta:
        db_table = 'aliases'

    def __str__(self):
        return self.id


class Card(models.Model):
    uid = models.CharField(primary_key=True, max_length=255)
    user = models.ForeignKey(User)
    added_date = models.DateTimeField()
    active = models.BooleanField()

    class Meta:
        db_table = 'cards'

    def __str__(self):
        return self.uid


class Interest(models.Model):
    interest_id = models.AutoField(primary_key=True)
    category = models.ForeignKey('InterestCategory', db_column='category')
    suggested = models.BooleanField()
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'interests'

    def __str__(self):
        return self.name


class InterestCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=255)

    class Meta:
        db_table = 'interests_categories'

    def __str__(self):
        return self.id


class Learning(models.Model):
    learning_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'learnings'

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'locations'

    def __str__(self):
        return self.name


class ProjectStates(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'project_states'

    def __str__(self):
        return self.name


class Project(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    state = models.ForeignKey(ProjectStates)
    location = models.ForeignKey(Location)
    location_name = models.CharField(db_column='location', max_length=255, blank=True, null=True)
    updated_date = models.DateTimeField()
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    contact = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.name


class ProjectLog(models.Model):
    timestamp = models.IntegerField()
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User, blank=True, null=True)
    details = models.CharField(max_length=255)

    class Meta:
        db_table = 'projects_logs'

    def __str__(self):
        return self.timestamp.strftime('%Y-%m-%d %H:%M:%S')


class Subscription(models.Model):
    user = models.ForeignKey(User)
    transaction = models.ForeignKey('Transaction')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        db_table = 'subscriptions'


class Transaction(models.Model):
    fit_id = models.TextField(unique=True)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return self.fit_id


class UserAlias(models.Model):
    user = models.ForeignKey(User)
    alias = models.ForeignKey(Alias)
    username = models.CharField(max_length=255)

    class Meta:
        db_table = 'users_aliases'
        unique_together = (('user', 'alias'),)

    def __str__(self):
        return self.alias.id


class UserInterest(models.Model):
    user = models.ForeignKey(User)
    interest = models.ForeignKey(Interest)

    class Meta:
        db_table = 'users_interests'
        unique_together = (('user', 'interest'),)

    def __str__(self):
        return self.interest


class UserLearning(models.Model):
    user = models.ForeignKey(User)
    learning = models.ForeignKey(Learning)

    class Meta:
        db_table = 'users_learnings'
        unique_together = (('user', 'learning'),)

    def __str__(self):
        return self.learning


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    allow_email = models.BooleanField()
    allow_doorbot = models.BooleanField()
    photo = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'users_profiles'
