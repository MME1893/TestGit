from django.db import models
from django.contrib.auth import models as auth_models


class UserManager(auth_models.BaseUserManager):

    def create_user(self, name , email, age, role , password = None , is_staff = False, is_superuser= False ) -> "User":
        if not email:
            raise ValueError("user must have an email")
        if not name:
            raise ValueError("user must have a name")
        if not age:
            raise ValueError("user must have an age")
        if not role:
            raise ValueError("user must have a role")

        user = self.model(email=self.normalize_email(email))
        user.name = name
        user.age = age
        user.role = role
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_superuser(self, name, email, age, role, password) -> "User":
        user = self.create_user(
            name= name,
            email=email,
            age=age,
            role=role,
            password= password,
            is_staff=True,
            is_superuser=True
        )

        user.save()

        return user




class User(auth_models.AbstractUser):
    name = models.CharField(verbose_name='Name', max_length=255)
    age = models.IntegerField(verbose_name='Age')
    role = models.CharField(verbose_name='Role',max_length=255)
    email = models.EmailField(verbose_name='Email',max_length=255, unique=True)
    password =  models.CharField(max_length=255)
    username = None


    object = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name" , "age" , "role"]

