# Generated by Django 2.1.2 on 2018-10-03 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_auto_20181002_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewresponse',
            old_name='response_text',
            new_name='response',
        ),
    ]