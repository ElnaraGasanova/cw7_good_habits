# Generated by Django 5.0.6 on 2024-06-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.IntegerField(choices=[(1, 'Ежедневно'), (2, 'Каждые 2 дня'), (3, 'Каждые 3 дня'), (4, 'Каждые 4 дня'), (5, 'Каждые 5 дней'), (6, 'Каждые 6 дней'), (7, 'Еженедельно')], default=1, help_text='Укажите периодичность выполнения', verbose_name='Периодичность выполнения в днях'),
        ),
    ]