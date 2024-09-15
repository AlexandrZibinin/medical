from django.urls import path

from main.apps import MainConfig
from main.views import (ContactsView, CompanyView, ServiceListView, ServiceDetailView,
                        AppointmentCreateView, AppointmentListView, AppointmentDetailView, AppointmentUpdateView,
                        AppointmentDeleteView, IndexView, )

app_name = MainConfig.name


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("company/", CompanyView.as_view(), name="company"),
    path("service/", ServiceListView.as_view(), name="service"),
    path("service/<int:pk>/", ServiceDetailView.as_view(), name="service_detail"),
    path("appointment/", AppointmentListView.as_view(), name="appointment"),
    path("appointment_create/", AppointmentCreateView.as_view(), name="appointment_create"),
    path("appointment/<int:pk>/", AppointmentDetailView.as_view(), name="appointment_detail"),
    path("appointment/<int:pk>/update/", AppointmentUpdateView.as_view(), name="appointment_update"),
    path("appointment/<int:pk>/delete/", AppointmentDeleteView.as_view(), name="appointment_delete"),
]
