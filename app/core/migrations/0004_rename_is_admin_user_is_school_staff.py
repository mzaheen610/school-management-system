# Generated by Django 3.2.23 on 2024-01-24 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_student_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_school_staff',
        ),
    ]
