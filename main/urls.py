from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('send_email', views.send_mail_to_all, name='send_mail_to_all'),
    path('schedule_email', views.schedule_email, name='schedule_email'),
]