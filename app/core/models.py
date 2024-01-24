"""
Models for the school management system.
[ user, student, staff, attendance ]
"""
from django.db import models
from django.contrib.auth import get_user_model
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
    is_school_staff = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["is_staff", "is_admin", "is_parent"]


class Student(models.Model):
    """Model for the student."""

    name = models.CharField(max_length=100, blank=False)
    student_id = models.AutoField(primary_key = True)
    date_of_birth = models.DateField()
    join_date = models.DateField(auto_now_add=True)
    current_class = models.CharField(max_length=10)
    email = models.EmailField(unique=True, blank=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        """Overriding default save method to auto create user for student's parent."""
        parent_email = self.email
        password = self.name
        user_model = get_user_model()
        user, created = user_model.objects.get_or_create(email=parent_email, defaults={'password': password, 'is_parent': True})

        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return f"{self.name} - ID{self.student_id}"