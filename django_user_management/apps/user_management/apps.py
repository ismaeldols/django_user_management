from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UserManagementConfig(AppConfig):
    name = 'django_user_management.apps.user_management'
    verbose_name = _('user_management')

    def ready(self):
        import django_user_management.apps.user_management.signals
