# Generated by Django 4.1.3 on 2022-12-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_gamer', '0003_rename_user_gamer_game_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='is_borrowed',
            field=models.BooleanField(choices=[(False, 'Free'), (True, 'In use')], default=False),
        ),
    ]