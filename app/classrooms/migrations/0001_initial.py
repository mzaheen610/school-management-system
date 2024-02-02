# Generated by Django 3.2.23 on 2024-01-31 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0007_auto_20240125_0709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('schedule_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('timetable_id', models.IntegerField(primary_key=True, serialize=False)),
                ('friday_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friday_schedule', to='classrooms.schedules')),
                ('monday_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monday_schedule', to='classrooms.schedules')),
                ('thursday_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thursday_schedule', to='classrooms.schedules')),
                ('tuesday_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_schedule', to='classrooms.schedules')),
                ('wednesday_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_schedule', to='classrooms.schedules')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('teacher_id', models.IntegerField(primary_key=True, serialize=False)),
                ('staff_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=255)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classrooms.teachers')),
            ],
        ),
        migrations.AddField(
            model_name='schedules',
            name='hr_five',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hr_five', to='classrooms.subject'),
        ),
        migrations.AddField(
            model_name='schedules',
            name='hr_four',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hr_four', to='classrooms.subject'),
        ),
        migrations.AddField(
            model_name='schedules',
            name='hr_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hr_one', to='classrooms.subject'),
        ),
        migrations.AddField(
            model_name='schedules',
            name='hr_seven',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hr_seven', to='classrooms.subject'),
        ),
        migrations.AddField(
            model_name='schedules',
            name='hr_six',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hr_six', to='classrooms.subject'),
        ),
        migrations.AddField(
            model_name='schedules',
            name='hr_three',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hr_three', to='classrooms.subject'),
        ),
        migrations.AddField(
            model_name='schedules',
            name='hr_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hr_two', to='classrooms.subject'),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.IntegerField(primary_key=True, serialize=False)),
                ('standard', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('room_no', models.IntegerField()),
                ('timetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classrooms.timetable')),
            ],
        ),
    ]