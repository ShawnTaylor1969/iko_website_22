from rest_framework.serializers import (
    ModelSerializer,
    )

from .models import Configuration

class ConfigurationCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Configuration
        fields = [
            'id', 'organization_name', 'domain_name', 'site_email_address', 'site_phone_number', 'main_background_color', 'primary_color', 'primary_light_color', 'secondary_color', 'secondary_light_color', 'brand_logo_img', 'header_background_img', 'log_in_img', 'sign_up_img', 'change_password_img', 'reset_password_img', 'successful_sign_up_msg', 'acceptable_use_policy'
        ]
class ConfigurationDetailSerializer(ModelSerializer):
    class Meta:
        model = Configuration
        fields = [
            'id', 'organization_name', 'domain_name', 'site_email_address', 'site_phone_number', 'main_background_color', 'primary_color', 'primary_light_color', 'secondary_color', 'secondary_light_color', 'brand_logo_img', 'header_background_img', 'log_in_img', 'sign_up_img', 'change_password_img', 'reset_password_img', 'successful_sign_up_msg', 'acceptable_use_policy'
        ]
