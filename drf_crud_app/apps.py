from django.apps import AppConfig
# from drf_crud_app import signals


class DrfCrudAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drf_crud_app'

    # def ready(self):
    #     import drf_crud_app.signals
