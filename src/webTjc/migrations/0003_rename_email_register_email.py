# Generated by Django 4.2.5 on 2023-09-30 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webTjc', '0002_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='email',
            new_name='Email',
        ),
    ]
