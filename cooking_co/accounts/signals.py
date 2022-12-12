from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from cooking_co import settings

UserModel = get_user_model()


@receiver(signal=post_save, sender=UserModel)
def send_email_on_successful_sign_up(instance, created, **kwargs):
    if not created:
        return

    email_content = render_to_string('common/email-greeting.html', {
        'user': instance})

    user_email = instance.email
    send_mail(
        subject='Welcome to Cooking Coach',
        message=strip_tags(email_content),
        html_message=email_content,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user_email,),
    )
