# Generated by Django 2.0.5 on 2018-08-21 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourWord', models.CharField(max_length=255)),
                ('yourColor', models.CharField(choices=[('Red', 'Red'), ('Green', 'Green'), ('Blue', 'Blue')], default='Blue', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50)),
                ('yourDojo', models.CharField(choices=[("Tyson's Corner", "Tyson's Corner"), ('Seattle', 'Seattle'), ('San Jose', 'San Jose')], default="Tyson's Corner", max_length=50)),
                ('yourLanguage', models.CharField(choices=[('Python', 'Python'), ('Javascript', 'Javascript'), ('Java', 'Java')], default='Python', max_length=50)),
                ('comment', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
