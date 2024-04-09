
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import College

class Add_college(CreateView):
    model = College
    fields = "__all__"


class List_college(ListView):
    model = College

class Detail_college(DetailView):
    model = College


class Update_college(UpdateView):
    model = College

    fields = "__all__"
    success_url = "/"

class Delete_college(DeleteView):
    model = College
    success_url = "/"
    template_name = "college/College_confirm.html"
