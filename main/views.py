from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from rest_framework.reverse import reverse_lazy

from main.forms import AppointmentForm
from main.models import Service, Appointment, Doctor


def index(request):
    return render(request, "index.html")

class ContactsView(TemplateView):
    template_name = "contacts_view.html"


class CompanyView(TemplateView):
    template_name = "company_view.html"

    def get_context_data(self, **kwargs):
        doctors = Doctor.objects.all()
        context = super().get_context_data(**kwargs)
        context['doctors'] = doctors
        return context

class ServiceListView(ListView):
    model = Service

class ServiceDetailView(DetailView):
    model = Service


class AppointmentListView(ListView):
    model = Appointment

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("main:appointment")

    def form_valid(self, form):
        appointment = form.save()
        user = self.request.user
        appointment.owner = user
        appointment.save()

        return super().form_valid(form)


class DoctorListView(ListView):
    model = Doctor








