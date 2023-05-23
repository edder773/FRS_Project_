from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter

class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    annual_income = models.IntegerField(null=True)
    occupation = models.CharField(max_length=20, null=True)
    assets = models.IntegerField(null=True)
    bank = models.CharField(max_length=15, null=True)
    location = models.CharField(max_length=25, null=True)
    age = models.IntegerField(null=True)
    financial_products = models.CharField(max_length=50, null=True)
    
        
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username

        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        annual_income = data.get("annual_income")
        occupation = data.get("occupation")
        assets = data.get("assets")
        bank = data.get("bank")
        location = data.get("location")
        age = data.get("age")
        financial_products = data.get("financial_products")

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname :
            user_field(user, "nickname", nickname)
        if annual_income:
            user.annual_income = annual_income
        if occupation:
            user_field(user, "occupation", occupation)
        if assets:
            user.assets = assets
        if bank:
            user_field(user, "bank", bank)
        if location:
            user_field(user, "location", location)
        if age :
            user.age = age
        if financial_products:
            user_field(user, "financial_products", financial_products)
        
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user

