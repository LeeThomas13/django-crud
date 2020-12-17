from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ComputerParts

class ComputerListView(ListView):
    template_name = 'comp-list.html'
    model = ComputerParts

class ComputerDetailView(ListView):
    template_name = 'comp-detail.html'
    model = ComputerParts

class ComputerCreateView(ListView):
    template_name = 'comp-create.html'
    model = ComputerParts

class ComputerUpdateView(ListView):
    template_name = 'comp-update.html'
    model = ComputerParts

class ComputerDeleteView(ListView):
    template_name = 'comp-delete.html'
    model = ComputerParts



