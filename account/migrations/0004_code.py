# Generated by Django 4.2.6 on 2023-10-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_phone_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('code', models.CharField(max_length=10)),
                ('token', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]