# Generated by Django 3.2.6 on 2021-09-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0011_auto_20210907_0134'),
    ]

    operations = [
        # migrations.RenameField(
        #     model_name='card',
        #     old_name='stats',
        #     new_name='attack',
        # ),
        migrations.AddField(
            model_name='card',
            name='defense',
            field=models.CharField(choices=[('-', '-'), ('No Good', 'No Good'), ('Decent', 'Decent'), ('Pretty Good', 'Pretty Good'), ('Very Good', 'Very Good'), ('Fantastic', 'Fantastic'), ('Best', 'Best')], default='-', max_length=12),
        ),
        migrations.AddField(
            model_name='card',
            name='hp',
            field=models.CharField(choices=[('-', '-'), ('No Good', 'No Good'), ('Decent', 'Decent'), ('Pretty Good', 'Pretty Good'), ('Very Good', 'Very Good'), ('Fantastic', 'Fantastic'), ('Best', 'Best')], default='-', max_length=12),
        ),
        migrations.AddField(
            model_name='card',
            name='attack',
            field=models.CharField(choices=[('-', '-'), ('No Good', 'No Good'), ('Decent', 'Decent'), ('Pretty Good', 'Pretty Good'), ('Very Good', 'Very Good'), ('Fantastic', 'Fantastic'), ('Best', 'Best')], default='-', max_length=12),
        ),
        migrations.AddField(
            model_name='card',
            name='sp_attack',
            field=models.CharField(choices=[('-', '-'), ('No Good', 'No Good'), ('Decent', 'Decent'), ('Pretty Good', 'Pretty Good'), ('Very Good', 'Very Good'), ('Fantastic', 'Fantastic'), ('Best', 'Best')], default='-', max_length=12),
        ),
        migrations.AddField(
            model_name='card',
            name='sp_defense',
            field=models.CharField(choices=[('-', '-'), ('No Good', 'No Good'), ('Decent', 'Decent'), ('Pretty Good', 'Pretty Good'), ('Very Good', 'Very Good'), ('Fantastic', 'Fantastic'), ('Best', 'Best')], default='-', max_length=12),
        ),
        migrations.AddField(
            model_name='card',
            name='speed',
            field=models.CharField(choices=[('-', '-'), ('No Good', 'No Good'), ('Decent', 'Decent'), ('Pretty Good', 'Pretty Good'), ('Very Good', 'Very Good'), ('Fantastic', 'Fantastic'), ('Best', 'Best')], default='-', max_length=12),
        ),
    ]
