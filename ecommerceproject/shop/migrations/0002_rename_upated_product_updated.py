# Generated by Django 3.2.17 on 2023-02-07 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='upated',
            new_name='updated',
        ),
    ]
