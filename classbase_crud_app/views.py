from django.shortcuts import render
from django.views.generic import CreateView, ListView, \
    DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import NameDetails


class NameCreateView(CreateView):
    model = NameDetails
    template_name = "name_form.html"
    fields = ["id", "person_name", "country_name"]
    success_url = reverse_lazy('name-list')


class NameListView(ListView):
    model = NameDetails
    template_name = 'name_list.html'
    context_object_name = 'namedetails'  # 'namedetails' in the template


class NameDetailView(DetailView):
    model = NameDetails
    template_name = 'name_detail.html'
    context_object_name = 'namedetail'


class NameUpdateView(UpdateView):
    model = NameDetails
    template_name = 'name_form.html'
    fields = ["id", "person_name", "country_name"]
    success_url = reverse_lazy('name-list')


class NameDeleteView(DeleteView):
    model = NameDetails
    context_object_name = 'namedetail'
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('name-list')
