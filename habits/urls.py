from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitCreateAPIView, HabitDetailAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, PublicHabitListApiView

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/<int:pk>/', HabitDetailAPIView.as_view(), name='habit_view'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('public/', PublicHabitListApiView.as_view(), name='habit_public'),
]
