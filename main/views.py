from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, "index.html")

class ContactsView(TemplateView):
    template_name = "contacts_view.html"

