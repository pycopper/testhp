# Generated by Django 3.2.5 on 2022-03-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('img', models.ImageField(upload_to='media/')),
                ('content', models.TextField(max_length=100)),
            ],
        ),
    ]
