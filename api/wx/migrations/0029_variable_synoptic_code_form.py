# Generated by Django 3.2.13 on 2024-08-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wx', '0028_auto_20240814_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='variable',
            name='synoptic_code_form',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
