from django.apps import AppConfig


from django.utils.translation import gettext_lazy as _


class NewsletterConfig(AppConfig):
    name = 'edavids.subscribe'
    verbose_name = _("Newsletters")
