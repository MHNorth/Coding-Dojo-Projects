# Generated by Django 2.0.5 on 2018-09-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiple_apps', '0005_auto_20180913_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='documentfile',
            field=models.FileField(blank=True, null=True, upload_to='documents/%D/'),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='imagefile',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%D/'),
        ),
    ]