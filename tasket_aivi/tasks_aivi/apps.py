from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TasksAiviConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks_aivi'


    class Meta:
        verbose_name = _('Tasks Aivi')