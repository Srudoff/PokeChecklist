# Generated by Django 3.2.6 on 2021-08-16 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0003_rename_name_card_poke_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='abilities',
        ),
        migrations.RemoveField(
            model_name='card',
            name='image',
        ),
        migrations.RemoveField(
            model_name='card',
            name='type1',
        ),
        migrations.RemoveField(
            model_name='card',
            name='type2',
        ),
    ]