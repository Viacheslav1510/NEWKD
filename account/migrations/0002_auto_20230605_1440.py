# Generated by Django 3.2.19 on 2023-06-05 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=30, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=20, unique=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=25, null=True)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=1)),
                ('age', models.PositiveSmallIntegerField()),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('county', models.CharField(choices=[('CORK', 'CORK'), ('GALWAY', 'GALWAY'), ('DONEGAL', 'DONEGAL'), ('MAYO', 'MAYO'), ('KERRY', 'KERRY'), ('TIPPERARY', 'TIPPERARY'), ('CLARE', 'CLARE'), ('TYRONE', 'TYRONE'), ('ANTRIM', 'ANTRIM'), ('LIMERICK', 'LIMERICK'), ('ROSCOMMON', 'ROSCOMMON'), ('DOWN', 'DOWN'), ('WEXFORD', 'WEXFORD'), ('MEATH', 'MEATH'), ('LONDONDERRY', 'LONDONDERRY'), ('KILKENNY', 'KILKENNY'), ('WICKLOW', 'WICKLOW'), ('OFFALY', 'OFFALY'), ('CAVAN', 'CAVAN'), ('WATERFORD', 'WATERFORD'), ('WESTMEATH', 'WESTMEATH'), ('SLIGO', 'SLIGO'), ('LAOIS', 'LAOIS'), ('KILDARE', 'KILDARE'), ('FERMANAGH', 'FERMANAGH'), ('LEITRIM', 'LEITRIM'), ('ARMAGH', 'ARMAGH'), ('MONOGHAN', 'MONOGHAN'), ('LONGFORD', 'LONGFORD'), ('DUBLIN', 'DUBLIN'), ('CARLOW', 'CARLOW'), ('LOUTH', 'LOUTH')], default='KERRY', max_length=20)),
                ('town_or_city', models.CharField(blank=True, max_length=30)),
                ('avatar', models.ImageField(blank=True, upload_to='profile_pics/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
