# Generated by Django 5.0.3 on 2024-03-30 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StockData',
            new_name='Data',
        ),
    ]
