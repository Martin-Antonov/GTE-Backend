from rest_framework import serializers

from customsettings.models import CustomSettings


class CustomSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomSettings
        exclude = ('id', 'user', )