from django.urls import path

from main.apps import MainConfig
from main.views import index, ContactsView

app_name = MainConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("contacts/", ContactsView.as_view(), name="contacts"),

]