"""
Models for the school management system.
[ user, student, staff, attendance ]
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin )

class UserManager(BaseUserManager):
    """Manager for users. """

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves the user."""
        if not email:
            raise ValueError("User must have an email")

        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and saves a superuser."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_parent', True)
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        user.is_superuser = True
        user.save(using=self._db)
        
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Model for the users."""
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, unique=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["is_staff", "is_admin", "is_parent"]

