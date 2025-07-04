import re

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'password',
        ]

    def validate_phone_number(self, value):
        if not value:
            raise serializers.ValidationError("Enter a valid phone number!")
        if not re.match(r'^\d{12}$', value):
            raise serializers.ValidationError("Format of phone number must be 12 digits!")
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("This phone number already exists!")
        return value

    def validate(self, attrs):
        print(attrs)
        user = User(
            username=attrs['username'],
            first_name=attrs['first_name'],
            last_name=attrs['last_name'],
            phone_number=attrs['phone_number'],
            email=attrs['email'],
            password=make_password(attrs['password']),
        )
        user.save()
        return super().validate(attrs)


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'phone_number',
        ]


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'email',
        ]
