from django.db import models
from colorful.fields import RGBColorField
from phone_field import PhoneField
from django.contrib.auth.models import User

class Configuration(models.Model):
    organization_name             = models.CharField(max_length=200, default='', blank=True)
    domain_name                   = models.CharField(max_length=200, default='', blank=True)
    site_email_address            = models.EmailField(max_length=256, default='', blank=True)
    site_phone_number             = PhoneField(blank=True, help_text='Site phone number')

    main_background_color         = RGBColorField()
    primary_color                 = RGBColorField()
    primary_light_color           = RGBColorField()
    secondary_color               = RGBColorField()
    secondary_light_color         = RGBColorField()

    brand_logo_img                = models.ImageField(upload_to='config_images', null=True, blank=True)
    header_background_img         = models.ImageField(upload_to='config_images', null=True, blank=True)
    log_in_img                    = models.ImageField(upload_to='config_images', null=True, blank=True)
    sign_up_img                   = models.ImageField(upload_to='config_images', null=True, blank=True)
    change_password_img           = models.ImageField(upload_to='config_images', null=True, blank=True)
    reset_password_img            = models.ImageField(upload_to='config_images', null=True, blank=True)

    successful_sign_up_msg        = models.TextField(default='Thank you for signing up!')

    acceptable_use_policy         = models.TextField()

def get_full_name(self):
    return self.first_name + " " + self.last_name

User.add_to_class("__str__", get_full_name)
