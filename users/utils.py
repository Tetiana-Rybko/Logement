from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(user_email, username):
    subject = 'Salut!'
    message = f'Hallo, {username}! thanks for registering.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)