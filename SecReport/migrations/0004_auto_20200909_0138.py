# Generated by Django 2.2.13 on 2020-09-09 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecReport', '0003_auto_20200906_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportviewpermission',
            name='hasPermission',
            field=models.BooleanField(default=False, verbose_name='Has permission?'),
        ),
    ]