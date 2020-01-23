# Generated by Django 3.0.2 on 2020-01-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=150)),
                ('product_name', models.CharField(max_length=150)),
                ('product_weight_g', models.IntegerField()),
                ('product_height_cm', models.IntegerField()),
                ('product_width_cm', models.IntegerField()),
                ('product_category', models.CharField(max_length=100)),
            ],
        ),
    ]