# Generated by Django 3.1.1 on 2020-09-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_management', '0010_auto_20200924_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='district',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='province',
            field=models.CharField(max_length=20, null=True, verbose_name='省级区划'),
        ),
    ]
