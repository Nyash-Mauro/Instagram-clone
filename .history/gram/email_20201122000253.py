from django.core.mail import send_mail

send_mail(
    'Welcome to the gram',
    '',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)