# Generated by Django 4.1.3 on 2022-12-08 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board_gamer', '0002_user_game_is_borrowed_game_borrower'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Gamer',
        ),
        migrations.AddField(
            model_name='game',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
