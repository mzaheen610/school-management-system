# Generated by Django 3.2.23 on 2024-01-23 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_birth', models.DateField()),
                ('join_date', models.DateField(auto_now_add=True)),
                ('current_class', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]