# Generated by Django 4.1.3 on 2022-11-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='banned',
            field=models.BooleanField(default=False),
        ),
    ]