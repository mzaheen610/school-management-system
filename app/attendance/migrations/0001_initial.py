# Generated by Django 3.2.23 on 2024-02-07 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0008_auto_20240207_0521'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present', max_length=10)),
                ('comment', models.CharField(blank=True, max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
            options={
                'unique_together': {('student', 'date')},
            },
        ),
        migrations.CreateModel(
            name='StaffAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present', max_length=10)),
                ('comment', models.CharField(blank=True, max_length=20)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.staff')),
            ],
            options={
                'unique_together': {('staff', 'date')},
            },
        ),
    ]