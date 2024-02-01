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
        extra_fields.setdefault('is_school_staff', True)
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
    REQUIRED_FIELDS = ["is_staff", "is_school_staff", "is_parent"]


class Student(models.Model):
    """Model for the student."""

    name = models.CharField(max_length=100, blank=False)
    student_id = models.CharField(max_length=10, primary_key=True, blank=True)
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
        user, created = user_model.objects.get_or_create(email=parent_email, defaults={'is_parent': True})

        user.set_password(password)
        user.save()
        if not self.user:
            self.user = user

        if not self.student_id:
            """Generate a unique student ID, example 'S001', S002"""
            last_student = Student.objects.order_by('-student_id').first()
            if last_student:
                last_id = int(last_student.student_id[1:])
                self.student_id = 'S{:03d}'.format(last_id + 1)
            else:
                self.student_id = 'S001'
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return f"{self.name} - ID {self.student_id}"


class Staff(models.Model):
    """Model for the school staff."""
    name = models.CharField(max_length=100, blank=False)
    staff_id = models.CharField(max_length=10, primary_key = True, blank=True)
    date_of_birth = models.DateField()
    join_date = models.DateField(auto_now_add=True)
    department_id = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True, blank=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        """Overriding default save method for staff."""

        staff_email = self.email
        password = self.name
        user_model = get_user_model()
        user, created = user_model.objects.get_or_create(email=staff_email, defaults={'is_school_staff': True})

        user.set_password(password)
        user.save()

        if not self.staff_id:
            # Generate a unique staff ID, for example, 'T001', 'T002', etc.
            last_staff = Staff.objects.order_by('-staff_id').first()
            if last_staff:
                last_id = int(last_staff.staff_id[1:])
                self.staff_id = 'T{:03d}'.format(last_id + 1)
            else:
                self.staff_id = 'T001'

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - ID {self.staff_id}"
