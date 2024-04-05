from django.db import models
import uuid
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django_jsonform.models.fields import ArrayField
from django.utils.translation import gettext_lazy as _

from user.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.TextField(max_length=30)
    username = models.TextField(max_length=30, unique=True)
    email = models.TextField(unique=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)

    is_verified = models.BooleanField(_('verified'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user') 
        verbose_name_plural = _('users')
        
    def __str__(self):
        return self.username
    
class UserData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.TextField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    fullname = models.TextField(null=True, blank=True)
    surname = models.TextField(null=True, blank=True)
    lastname = models.TextField(null=True, blank=True)
    phone_number = models.TextField(unique=True, null=True, blank=True)
    contact_telegram = models.TextField(unique=True, null=True, blank=True)
    contact_email = models.TextField(unique=True, null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    sex = models.TextField(null=True, blank=True)
    graduation_place = models.TextField(null=True, blank=True)
    graduation_date = models.DateField(null=True, blank=True)
    languages = ArrayField(models.CharField(max_length=20, blank=True), null=True, blank=True)
    curses = ArrayField(models.TextField(blank=True), null=True, blank=True)
    picture = models.ImageField(upload_to='profile_photo/', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)

class UserSkills(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    skills = ArrayField(models.TextField(blank=True), null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)
    
class UserExperience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    experience = ArrayField(models.TextField(blank=True), null=True, )
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)