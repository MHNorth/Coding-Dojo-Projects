from . models import Paste
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView


class PasteCreate(CreateView):
    model = Paste
    fields = ['title', 'text', 'name']

class PasteDetail(DetailView):
    model = Paste
    template_name = "pastebin/paste_detail.html"

class PasteList(ListView):
    model = Paste
    template_name = "pastebin/paste_list.html"
    queryset = Paste.objects.all()
    context_object_name = 'queryset'

class PasteDelete(DeleteView):
    model = Paste
    success_url = reverse_lazy('pastebin_paste_list')

class PasteUpdate(UpdateView):
    model = Paste
    fields = ['title', 'text', 'name']