# Generated by Django 2.2.3 on 2019-07-26 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0008_auto_20190726_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='registration',
        ),
        migrations.AddField(
            model_name='registration',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homeapp.Event'),
        ),
    ]
