# Generated by Django 2.2.6 on 2019-11-11 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20191111_0535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gif',
            old_name='image',
            new_name='image_url',
        ),
    ]
