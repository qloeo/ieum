# Generated by Django 3.2.18 on 2023-05-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paints', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paint',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
