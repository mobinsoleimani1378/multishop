# Generated by Django 4.2.6 on 2023-10-28 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
