# Generated by Django 3.2.23 on 2024-01-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20240124_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='department_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]