# Generated by Django 3.1.3 on 2022-12-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0013_auto_20221222_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackinghistory',
            name='mobilenum',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
