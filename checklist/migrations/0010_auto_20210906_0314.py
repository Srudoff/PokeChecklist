# Generated by Django 3.2.6 on 2021-09-06 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0009_auto_20210826_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='poke_sprite',
            field=models.ImageField(default=1, upload_to=''),
        ),
        migrations.AddField(
            model_name='card',
            name='shiny_sprite',
            field=models.ImageField(default=1, upload_to=''),
        ),
        # migrations.AddField(
        #     model_name='card',
        #     name='stats',
        #     field=models.CharField(choices=[('-', '-'), ('No Good', 'No Good'), ('Decent', 'Decent'), ('Pretty Good', 'Pretty Good'), ('Very Good', 'Very Good'), ('Fantastic', 'Fantastic'), ('Best', 'Best')], default='-', max_length=12),
        # ),
    ]
