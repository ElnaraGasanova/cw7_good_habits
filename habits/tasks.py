from datetime import timedelta
from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from habits.services import send_tg_message


# тестовая задача проверки celery
# @shared_task
# def send_tg_habits_reminder():
#     today = timezone.now().today().date
#     print(today)


@shared_task
def send_tg_habits_reminder():
    '''ТГ-рассылка напоминаний о том, в какое время и какие
    привычки необходимо выполнять, если дата выполнения - сегодня.'''
    today = timezone.now()       # .today().date отобразится в формате даты
    habits = Habit.objects.all()     # фильтруем привычки
    message = f'Привет! Выполни {habits.action} {habits.time}, место - {habits.location}'
    # telegram_id_list = []     # выводим список привычек

    for habit in habits:
        if habit.owner.telegram_id and habit.time >= today:
            send_tg_message(habit.owner.telegram_id, message)
        # telegram_id_list.append(habit.owner.telegram_id)
        if habit.periodicity == '1':
            habit.time = today + timedelta(days=1)
        elif habit.periodicity == '2':
            habit.time = today + timedelta(days=2)
        elif habit.periodicity == '3':
            habit.time = today + timedelta(days=3)
        elif habit.periodicity == '2':
            habit.time = today + timedelta(days=4)
        elif habit.periodicity == '2':
            habit.time = today + timedelta(days=5)
        elif habit.periodicity == '2':
            habit.time = today + timedelta(days=6)
        else:
            habit.time = today + timedelta(days=7)
        habit.save()
