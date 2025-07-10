# mailer/urls.py
from django.urls import path
from .views import send_mail_view

urlpatterns = [
    path('send/', send_mail_view, name='send_mail'),  # ✅ Name must match the one used in HTML
]
