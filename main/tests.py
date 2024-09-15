from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from main.models import Service, Doctor, Appointment
from users.models import User


class TestMain(TestCase):

    def setUp(self):
        self.service = Service.objects.create(name="Test_service1",
                                              description="Диагностика тестовая",
                                              price=10)
        self.user = User.objects.create(email='testuser@example.com', name="TestNameUser")
        self.doctor = Doctor.objects.create(name="TestNameDoctor")
        self.appointment = Appointment.objects.create(owner=self.user, service=self.service, doctor=self.doctor,
                                                      date_at="2024-01-01 00:00")

    def test_create_appointment(self):

        data = {
            "owner": self.user,
            "service": self.service,
            "doctor": self.doctor,
            "date_at": "2024-01-01 00:00"
        }
        self.create = reverse('main:appointment_create')
        response = self.client.post(self.create, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Appointment.objects.all().count(), 1)
        self.assertEqual(self.appointment.user.email, 'testuser@example.com')
        self.assertEqual(self.appointment.service.name, "TestNameUser")
        self.assertEqual(self.appointment.doctor.name, "TestNameDoctor")

    def test_list_appointment(self):
        self.list_url = reverse('main:appointment')
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'main/appointment.html')

    def test_delete_appointment(self):

        url = reverse("main:appointment_delete", args=(self.appointment.pk,))
        data = {
            "user": self.user,
            "service": self.service,
            "doctor": self.doctor,
            "date_at": "2024-01-01 00:00"
        }

        response = self.client.delete(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_edit_appointment(self):

        url = reverse("main:appointment_update", args=(self.record.pk,))
        doctor = Doctor.objects.create(name="TestNameDoctor1", )

        data = {
            "user": self.user,
            "service": self.service,
            "doctor": doctor,
            "date_at": "2024-01-01 00:00"
        }

        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Appointment.objects.all().count(), 1)
        self.assertEqual(self.appointment.user.email, 'testuser@example.com')
        self.assertEqual(self.appointment.service.name, "TEST1")
        self.assertEqual(self.appointment.doctor.name, "TestNameDoctor1")

    def tearDown(self):
        pass
