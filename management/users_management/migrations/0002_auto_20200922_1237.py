# Generated by Django 3.1.1 on 2020-09-22 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论'},
        ),
    ]
