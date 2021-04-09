from django.core.mail import EmailMessage
from rest_framework.permissions import BasePermission
from django.conf import settings


class Util:
    """Send mail"""
    @staticmethod
    def send_email(data):
        FORM_EMAIL = settings.FORM_EMAIL
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], from_email=FORM_EMAIL, to=[data['to_email']]
        )
        email.send()


class IsAuthorize(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
