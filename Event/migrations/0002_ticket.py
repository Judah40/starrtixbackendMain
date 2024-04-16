# Generated by Django 5.0.3 on 2024-03-27 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketnumber', models.IntegerField()),
                ('expirationdate', models.DateField()),
                ('ticketsold', models.IntegerField()),
                ('ticketleft', models.IntegerField()),
                ('ticketscanned', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.event')),
            ],
        ),
    ]