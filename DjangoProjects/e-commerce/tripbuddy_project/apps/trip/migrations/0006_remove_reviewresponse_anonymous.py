# Generated by Django 2.1.2 on 2018-10-03 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0005_auto_20181003_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewresponse',
            name='anonymous',
        ),
    ]
