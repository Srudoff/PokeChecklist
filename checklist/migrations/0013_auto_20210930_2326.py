# Generated by Django 3.2.6 on 2021-09-30 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0012_auto_20210930_0435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='attack',
            new_name='attack_iv',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='defense',
            new_name='defense_iv',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='hp',
            new_name='hp_iv',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='sp_attack',
            new_name='sp_attack_iv',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='sp_defense',
            new_name='sp_defense_iv',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='speed',
            new_name='speed_iv',
        ),
        migrations.AddField(
            model_name='card',
            name='attack_ev',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='card',
            name='defense_ev',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='card',
            name='hp_ev',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='card',
            name='sp_attack_ev',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='card',
            name='sp_defense_ev',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='card',
            name='speed_ev',
            field=models.SmallIntegerField(default=0),
        ),
    ]