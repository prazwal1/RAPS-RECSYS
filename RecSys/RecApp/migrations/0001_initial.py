# Generated by Django 3.0.3 on 2020-03-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('product_id', models.CharField(db_index=True, max_length=150, unique=True)),
                ('product_index', models.IntegerField(primary_key=True, serialize=False)),
                ('review_score', models.FloatField()),
                ('seller_index', models.IntegerField()),
                ('category_index', models.FloatField()),
                ('sales_count', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['product_index'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(db_index=True, max_length=150, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=150)),
                ('product_weight_g', models.FloatField()),
                ('product_length_cm', models.FloatField()),
                ('product_height_cm', models.FloatField()),
                ('product_width_cm', models.FloatField()),
                ('product_category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'ordering': ['?'],
            },
        ),
    ]
