from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
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


class AppointmentListView(ListView, LoginRequiredMixin):
    model = Appointment

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class AppointmentCreateView(CreateView, LoginRequiredMixin):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("main:appointment")

    def form_valid(self, form):
        appointment = form.save()
        user = self.request.user
        appointment.owner = user
        appointment.save()

        return super().form_valid(form)


class AppointmentDetailView(DetailView, LoginRequiredMixin):
    model = Appointment

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied


class AppointmentUpdateView(DetailView, LoginRequiredMixin):
    model = Appointment
    fields = ('date_at', 'service', 'doctor',)
    success_url = reverse_lazy('main:appointment')


class AppointmentDeleteView(DetailView, LoginRequiredMixin):
    model = Appointment
    success_url = reverse_lazy('main:appointment')


class DoctorListView(ListView):
    model = Doctor









