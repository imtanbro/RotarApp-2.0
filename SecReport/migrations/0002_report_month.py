# Generated by Django 2.2.13 on 2020-10-18 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SecReport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='month',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='SecReport.Month'),
        ),
    ]