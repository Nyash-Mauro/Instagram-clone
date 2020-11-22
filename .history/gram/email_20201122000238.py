from django.core.mail import send_mail

send_mail(
    'We',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)