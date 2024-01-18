from rest_framework import serializers
from account.models import MyUser
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.utils import SendEmail


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["username", "first_name", "last_name", "email", "password", "is_admin", "role"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = MyUser
        fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role', 'is_admin']


# class UserChangePasswordSerializer(serializers.Serializer):
#     password = serializers.CharField(
#         max_length=255, style={'input_type': 'password'}, write_only=True)
#     password2 = serializers.CharField(
#         max_length=255, style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         fields = ['password', 'password2']

#     def validate(self, attrs):
#         password = attrs.get('password')
#         password2 = attrs.get('password2')
#         user = self.context.get('user')
#         if password != password2:
#             raise serializers.ValidationError(
#                 "Password and Confirm Password do not match")

#         user.set_password(password)
#         user.save()
#         return attrs
