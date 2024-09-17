from django.contrib import admin

from main.models import Doctor, Service, Appointment, ContactsCompany, ResultAppointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_filter = ("name",)
    search_fields = ("name", "description")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_filter = ("name",)
    search_fields = ("name", "description")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("date_at", "service", "doctor", "owner", "result",)
    list_filter = ("date_at", "service", "doctor", "owner", "result",)
    search_fields = ("date_at", "service", "doctor", "owner", "result",)


@admin.register(ContactsCompany)
class ContactsCompanyAdmin(admin.ModelAdmin):
    list_display = ("address", "image", "phone", "email",)


@admin.register(ResultAppointment)
class ResultAppointmentAdmin(admin.ModelAdmin):
    list_display = ("date", "result",)
