from django.core.mail import send_mail

send_mail(
    'Welcome to the gram {{user}}',
    'Hope you will love it',
    'cheatcodes.dev.com',
    ['to@example.com'],
    fail_silently=False,
)