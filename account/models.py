from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
        Custom user class that inherits from the abstactuser class
        of django.
    """
    username = models.CharField(max_length=20, unique=True, db_index=True)
    email = models.EmailField(_('email address'), unique=True, max_length=30)
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        db_table = 'auth_user'


class Profile(models.Model):
    """
        User's profile to enable avatar, address, firstname,
        lastname and etc.

    """
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    COUNTY_CHOICES = [
        ('CORK', 'CORK'),
        ('GALWAY', 'GALWAY'),
        ('DONEGAL', 'DONEGAL'),
        ('MAYO', 'MAYO'),
        ('KERRY', 'KERRY'),
        ('TIPPERARY', 'TIPPERARY'),
        ('CLARE', 'CLARE'),
        ('TYRONE', 'TYRONE'),
        ('ANTRIM', 'ANTRIM'),
        ('LIMERICK', 'LIMERICK'),
        ('ROSCOMMON', 'ROSCOMMON'),
        ('DOWN', 'DOWN'),
        ('WEXFORD', 'WEXFORD'),
        ('MEATH', 'MEATH'),
        ('LONDONDERRY', 'LONDONDERRY'),
        ('KILKENNY', 'KILKENNY'),
        ('WICKLOW', 'WICKLOW'),
        ('OFFALY', 'OFFALY'),
        ('CAVAN', 'CAVAN'),
        ('WATERFORD', 'WATERFORD'),
        ('WESTMEATH', 'WESTMEATH'),
        ('SLIGO', 'SLIGO'),
        ('LAOIS', 'LAOIS'),
        ('KILDARE', 'KILDARE'),
        ('FERMANAGH', 'FERMANAGH'),
        ('LEITRIM', 'LEITRIM'),
        ('ARMAGH', 'ARMAGH'),
        ('MONOGHAN', 'MONOGHAN'),
        ('LONGFORD', 'LONGFORD'),
        ('DUBLIN', 'DUBLIN'),
        ('CARLOW', 'CARLOW'),
        ('LOUTH', 'LOUTH'),
    ]
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        default=FEMALE,
        max_length=1
        )
    age = models.IntegerField(default=14)
    address = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(
        max_length=20,
        choices=COUNTY_CHOICES,
        default='KERRY'
        )
    town_or_city = models.CharField(blank=True, max_length=30)
    avatar = models.ImageField(blank=True, upload_to='profile_pics/')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def image_tag(self):
        if self.avatar:
            return mark_safe(
                '<img src="%s" height="50" width="50">' % self.avatar.url
                )
        return "No image found"

    def __str__(self):
        return self.user.username
