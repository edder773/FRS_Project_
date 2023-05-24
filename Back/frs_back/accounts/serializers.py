from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from allauth.utils import email_address_exists, get_username_max_length
from allauth.account import app_settings as allauth_account_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.utils.translation import gettext_lazy as _

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_account_settings.USERNAME_MIN_LENGTH,
        required=allauth_account_settings.USERNAME_REQUIRED,
    )
    email = serializers.EmailField(required=allauth_account_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    nickname = serializers.CharField(max_length=50)
    annual_income = serializers.IntegerField(required=False)
    occupation = serializers.CharField(max_length=20, required=False)
    assets = serializers.IntegerField(required=False)
    bank = serializers.CharField(max_length=15, required=False)
    address = serializers.CharField(max_length = 25, required=False)
    age = serializers.IntegerField(required=False)
    financial_products = serializers.CharField(max_length=150, required=False)

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_account_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _('A user is already registered with this e-mail address.'),
                )
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'annual_income': self.validated_data.get('annual_income', ''),
            'occupation': self.validated_data.get('occupation', ''),
            'assets': self.validated_data.get('assets', ''),
            'bank': self.validated_data.get('bank', ''),
            'address': self.validated_data.get('address', ''),
            'age': self.validated_data.get('age', ''),
            'financial_products' : self.validated_data.get('financial_products',''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
            )
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

from .models import User
from django.conf import settings
class UserDetailsSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_username(username):
        if 'allauth.account' not in settings.INSTALLED_APPS:
            return username

        from allauth.account.adapter import get_adapter
        username = get_adapter().clean_username(username)
        return username

    class Meta:
        extra_fields = []
        if hasattr(User, 'USERNAME_FIELD'):
            extra_fields.append(User.USERNAME_FIELD)
        if hasattr(User, 'EMAIL_FIELD'):
            extra_fields.append(User.EMAIL_FIELD)
        if hasattr(User, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(User, 'annual_income'):
            extra_fields.append('annual_income')
        if hasattr(User, 'assets'):
            extra_fields.append('assets')
        if hasattr(User, 'bank'):
            extra_fields.append('bank')
        if hasattr(User, 'address'):
            extra_fields.append('address')
        if hasattr(User, 'age'):
            extra_fields.append('age')
        if hasattr(User, 'financial_products'):
            extra_fields.append('financial_products')

        model = User
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)
        
class ProfileChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','nickname','email','annual_income','occupation','assets','bank','address','age')