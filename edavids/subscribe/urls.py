from django.urls import path

from .views import (
    SubscriberView,
    confirm,
    delete,
)

app_name = "newsletter"
urlpatterns = [
    path("~subscriber/", view=SubscriberView.as_view(), name="subscribe"),
    path("~confirm/", view=confirm, name="confirm"),
    path("~delete/", view=delete, name="delete"),
]
