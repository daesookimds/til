# Generated by Django 2.2.7 on 2019-11-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='uesrname',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
    ]
