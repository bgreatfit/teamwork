# Generated by Django 2.2.6 on 2019-11-18 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20191117_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories', to='backend.Category'),
        ),
    ]
