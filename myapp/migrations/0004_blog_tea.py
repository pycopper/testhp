# Generated by Django 4.0.3 on 2022-04-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_content_blog_contents'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tea',
            field=models.BooleanField(default=False),
        ),
    ]
