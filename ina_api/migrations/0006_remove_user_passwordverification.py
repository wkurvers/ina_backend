# Generated by Django 2.1.3 on 2018-12-19 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ina_api', '0005_user_passwordverification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='passwordVerification',
        ),
    ]
