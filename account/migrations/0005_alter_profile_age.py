# Generated by Django 3.2.19 on 2023-06-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=1, max_length=3),
        ),
    ]