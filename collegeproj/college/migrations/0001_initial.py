# Generated by Django 5.0.4 on 2024-04-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=20)),
                ('college_address', models.CharField(max_length=20)),
                ('principal', models.CharField(max_length=20)),
                ('total_students', models.IntegerField()),
                ('total_teachers', models.IntegerField()),
            ],
        ),
    ]
