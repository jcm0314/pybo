# Generated by Django 3.1.3 on 2024-02-07 12:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_auto_20240207_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]