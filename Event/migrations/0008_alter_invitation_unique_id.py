# Generated by Django 4.2 on 2024-04-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0007_event_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='unique_id',
            field=models.PositiveIntegerField(editable=False, unique=True),
        ),
    ]