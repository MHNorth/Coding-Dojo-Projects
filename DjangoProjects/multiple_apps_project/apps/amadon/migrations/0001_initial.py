# Generated by Django 2.0.5 on 2018-08-21 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryList', models.CharField(choices=[('Beauty and Spa', 'Beauty and Spa'), ('Soundtrack Music', 'Soundtrack Music'), ("Women's Clothing", "Women's Clothing")], default='Beauty and Spa', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amadon.ProductCategorie'),
        ),
    ]