from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from .forms import PetForm
from .models import Pet

class PetCreate(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/create.html'
    success_url = reverse_lazy('pet_list')

    def form_valid(self, form):
    	pet = form.save(commit=False)
        pet.owner = self.request.user
        return super(PetCreate, self).form_valid(form)

class PetUpdate(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/edit.html'
    success_url = reverse_lazy('pet_list')


class PetDelete(DeleteView):
    model = Pet
    success_url = reverse_lazy('pet_list')

class PetList(ListView):
    model = Pet
    template_name = 'pet/index.html'

    def get_queryset(self):
    	cat = self.request.GET.get('cat', None)
    	queryset = Pet.objects.all()
    	if not cat:
    		return queryset
    	if cat == 'mine':
    		queryset = Pet.objects.filter(owner=self.request.user)
    	return queryset

class PetDetail(DetailView):
    model = Pet
    template_name = 'pet/detail.html'
