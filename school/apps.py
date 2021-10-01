from django.apps import AppConfig
from .views import home

class SchoolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'school'
    def meta():
        title = title
