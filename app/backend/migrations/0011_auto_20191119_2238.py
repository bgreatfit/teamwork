# Generated by Django 2.2.6 on 2019-11-19 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0010_auto_20191118_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'article_comment',
            },
        ),
        migrations.CreateModel(
            name='GIFComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gif', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='gif_comments', to='backend.GIF')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='gif_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'gif_comment',
            },
        ),
        migrations.RemoveField(
            model_name='flag',
            name='comment',
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='categories', to='backend.Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='article',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to='backend.Article'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flag',
            name='article_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flags', to='backend.ArticleComment'),
        ),
        migrations.AddField(
            model_name='flag',
            name='gif_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flags', to='backend.GIFComment'),
        ),
    ]
