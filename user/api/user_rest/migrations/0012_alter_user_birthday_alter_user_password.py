# Generated by Django 4.0.3 on 2023-03-15 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_rest', '0011_alter_rental_amenity_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='!nMCUSlg79VmChqtsMl9FNtky65zZJQOHiAgcdAsw', max_length=128),
        ),
    ]