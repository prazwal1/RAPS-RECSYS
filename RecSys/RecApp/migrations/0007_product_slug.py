# Generated by Django 3.0.2 on 2020-01-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecApp', '0006_auto_20200122_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]