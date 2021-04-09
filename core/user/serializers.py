from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credential')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('country_tag', 'source_tag', 'keyword_tag')

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        country_tag = validated_data.get('country_tag', None)
        source_tag = validated_data.get('source_tag', None)
        keyword_tag = validated_data.get('keyword_tag', None)
        user = super().update(instance, validated_data)

        Profile.objects.filter(user=user).update(country_tag=country_tag, source_tag=source_tag, keyword_tag=keyword_tag)
        return user


class PasswordRestEmailSerializer(serializers.Serializer):
    """Password reset request mail serializer"""

    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']

