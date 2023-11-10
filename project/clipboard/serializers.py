from rest_framework import serializers
from clipboard.models import Clipboard
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class ClipboardSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Clipboard
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    clipboards = serializers.PrimaryKeyRelatedField(many=True, queryset=Clipboard.objects.all())

    class Meta:
        model = User
        fields = ['uuid', 'username', 'clipboards']


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user