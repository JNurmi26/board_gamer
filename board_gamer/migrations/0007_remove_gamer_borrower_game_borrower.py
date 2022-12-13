# Generated by Django 4.1.3 on 2022-12-13 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board_gamer', '0006_remove_game_borrower_gamer_borrower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamer',
            name='borrower',
        ),
        migrations.AddField(
            model_name='game',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='board_gamer.gamer'),
        ),
    ]
