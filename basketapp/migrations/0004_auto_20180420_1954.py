# Generated by Django 2.0.4 on 2018-04-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0003_player_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photograpy',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
