# Generated by Django 3.2.4 on 2022-01-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
