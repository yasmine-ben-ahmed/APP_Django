# Generated by Django 4.1.7 on 2023-04-08 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0006_client_supervisor_supervisor_supervisor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='nom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='prenom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]