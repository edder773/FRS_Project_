from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from deposits.models import DepositProducts

class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    annual_income = models.IntegerField(null=True)
    occupation = models.CharField(max_length=20, null=True)
    assets = models.IntegerField(null=True)
    bank = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=25, null=True)
    age = models.IntegerField(null=True)
    products = models.CharField(max_length=100, null=True,)
    financial_products = models.ManyToManyField(DepositProducts, related_name='users', blank=True)
    
        
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
        address = data.get("address")
        age = data.get("age")
        products = data.get("products")
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
        if address:
            user_field(user, "address", address)
        if age :
            user.age = age
        if financial_products:
            for product_id in financial_products:
                product = DepositProducts.objects.get(id=product_id)
                user.financial_products.add(product)
        if products:
            user_field(user, "products", products)
        
        
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user

