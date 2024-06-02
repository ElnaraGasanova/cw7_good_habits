# Generated by Django 5.0.6 on 2024-06-02 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='action',
            field=models.CharField(choices=[('cycling', 'велопрогулка'), ('water', 'пить_воду'), ('reading', 'чтение'), ('fitness', 'фитнес')], help_text='Укажите действие привычки', max_length=200, verbose_name='Что выполнить'),
        ),
    ]