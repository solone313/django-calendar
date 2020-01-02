from django.urls import path
from .views import *

app_name = 'django_calendar'

urlpatterns = [
    path('monthly/', MakeMonthly.as_view(),),
    path('monthly/<int:year>/<int:month>/<int:day>/', MakeMonthly.as_view(), name='monthly'),
    path('schedule_data/', ScheduleListView.as_view(), name='schedule_data'),

] 