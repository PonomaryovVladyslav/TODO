# Generated by Django 3.1.2 on 2020-10-30 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200307_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'permissions': [('to_check_groups', 'Bla bla')], 'verbose_name': 'Zametka', 'verbose_name_plural': 'Zametki'},
        ),
    ]
