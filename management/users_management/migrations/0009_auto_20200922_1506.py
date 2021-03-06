# Generated by Django 3.1.1 on 2020-09-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_management', '0008_auto_20200922_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('province', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'access',
            },
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='access',
        ),
    ]
