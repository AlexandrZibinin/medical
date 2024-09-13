from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy("users:login")