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
    position = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    fullname = models.TextField(null=True, blank=True)
    surname = models.TextField(null=True, blank=True)
    lastname = models.TextField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    contact_telegram = models.TextField(null=True, blank=True)
    contact_email = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    sex = models.TextField(null=True, blank=True)
    graduation_place = models.TextField(null=True, blank=True)
    education_level = models.CharField(null=True, blank=True)
    graduation_date = models.DateField(null=True, blank=True)
    languages = ArrayField(models.CharField(blank=True, null=True), null=True, blank=True)
    curses = ArrayField(models.CharField(blank=True, null=True), null=True, blank=True)
    picture = models.ImageField(upload_to='profile_photo/', null=True, blank=True)
    coordinate_x = models.FloatField(null=True, blank=True)
    coordinate_y = models.FloatField(null=True, blank=True)
    color = models.CharField(null=True, blank=True)
    border_radius = models.FloatField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)

class UserSkills(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    skills = ArrayField(models.CharField(blank=True), null=True, blank=True)
    coordinate_x = models.FloatField(null=True, blank=True)
    coordinate_y = models.FloatField(null=True, blank=True)
    color = models.CharField(null=True, blank=True)
    border_radius = models.FloatField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)
    
class UserExperience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    experience_years = models.CharField(null=True, blank=True)
    position = models.CharField(null=True, blank=True)
    company = models.CharField(null=True, blank=True)
    experience_info = models.CharField(null=True, blank=True)
    coordinate_x = models.FloatField(null=True, blank=True)
    coordinate_y = models.FloatField(null=True, blank=True)
    color = models.CharField(null=True, blank=True)
    border_radius = models.FloatField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)
    
class UserVacancy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)   
    username  = models.CharField(null=True, blank=True)
    status = models.CharField(default = "NONE", null=True, blank=True)
    hh_id = models.CharField(null=True, blank=True)
    name = models.CharField( null=True, blank=True)
    area = models.CharField(null=True, blank=True)
    salary_from = models.CharField(null=True, blank=True)
    salary_to = models.CharField(null=True, blank=True)
    address = models.CharField(null=True, blank=True)
    url = models.CharField(null=True, blank=True)
    company = models.CharField(null=True, blank=True)
    requirements = models.CharField(null=True, blank=True)
    responsobility = models.CharField(null=True, blank=True)
    scedule = models.CharField(null=True, blank=True)
    role = models.CharField(null=True, blank=True)
    experience = models.CharField(null=True, blank=True)
    time_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.user_id)

class Sphere(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sphere = models.CharField(max_length=50)

    def __str__(self):
        return self.sphere

class Hashtag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hashtag = models.CharField(max_length=50)

    def __str__(self):
        return self.hashtag


class Portfolio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio_html=models.TextField(null=True, blank=True)
    portfolio_text=models.TextField(null=True, blank=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    sphere_id = models.ForeignKey('Sphere', on_delete=models.CASCADE, null=True, blank=True)
    public = models.BooleanField(default=True)
    # heading_ids = models.ManyToManyField('user.Heading', related_name='porfolio_headings', null=True, blank=True)
    # link_ids = models.ManyToManyField('user.Link', related_name='porfolio_links', null=True, blank=True)
    # textfield_ids = models.ManyToManyField('user.TextField', related_name='porfolio_textfields', null=True, blank=True)
    # list_ids = models.ManyToManyField('user.List', related_name='porfolio_lists', null=True, blank=True)
    # photo_ids = models.ManyToManyField('user.Photo', related_name='porfolio_photos', null=True, blank=True)
    # slider_ids = models.ManyToManyField('user.Slider', related_name='porfolio_sliders', null=True, blank=True)
    hashtag_ids = models.ManyToManyField('user.Hashtag', related_name='porfolio_hashtags', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)
    

class Heading(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.TextField()
    font = models.CharField()
    size = models.FloatField()
    color = models.CharField()
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()
    coordinate_z = models.IntegerField()
    transparency = models.FloatField()
    italics = models.BooleanField(default=False)
    bold = models.BooleanField(default=True)
    underlining = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value

class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.TextField()
    font = models.CharField()
    size = models.FloatField()
    color = models.CharField()
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()
    coordinate_z = models.IntegerField()
    transparency = models.FloatField()
    italics = models.BooleanField(default=True)
    bold = models.BooleanField(default=False)
    underlining = models.BooleanField(default=True) 
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value

class TextField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio_id = models.ForeignKey('Portfolio', on_delete=models.CASCADE, null=True)
    value = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    font = models.CharField(null=True, blank=True)
    size = models.FloatField(null=True, blank=True)
    color = models.CharField(null=True, blank=True)
    coordinate_x = models.FloatField(null=True, blank=True)
    coordinate_y = models.FloatField(null=True, blank=True)
    coordinate_z = models.IntegerField(null=True, blank=True)
    transparency = models.FloatField(null=True, blank=True)
    italics = models.BooleanField(default=False)
    bold = models.BooleanField(default=True)
    underlining = models.BooleanField(default=False) 
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    border = models.BooleanField(default=False)
    border_color = models.CharField(null=True, blank=True) 
    border_transparency = models.FloatField(null=True, blank=True)   
    border_radius = models.FloatField(null=True, blank=True)
    border_width = models.FloatField(null=True, blank=True) 
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value


class List(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.TextField()
    font = models.CharField()
    size = models.FloatField()
    color = models.CharField()
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()
    coordinate_z = models.IntegerField()
    transparency = models.FloatField()
    italics = models.BooleanField(default=True)
    bold = models.BooleanField(default=False)
    underlining = models.BooleanField(default=True)  
    list_values = ArrayField(models.TextField(blank=True), null=True, )
    font_list = models.CharField()
    size_list = models.FloatField()
    color_list = models.CharField()
    transparency_list = models.FloatField()
    italics_list = models.BooleanField(default=True)
    bold_list = models.BooleanField(default=False)
    underlining_list = models.BooleanField(default=True) 
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.value


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio_id = models.ForeignKey('Portfolio', on_delete=models.CASCADE, null=True)
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()
    coordinate_z = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField() 
    picture = models.ImageField(upload_to='portfolio_photo/', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Slider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio_id = models.ForeignKey('Portfolio', on_delete=models.CASCADE, null=True)
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()
    coordinate_z = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    # pictures =  ArrayField(models.ImageField(upload_to='portfolio_slider/', null=True, blank=True), null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)    
    
class SliderImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slider_id = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='pictures')
    image = models.ImageField(upload_to='portfolio_slider/')   

    def __str__(self):
        return str(self.id) 