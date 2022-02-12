from audioop import reverse
from attr import field
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from .models import owner , pet
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django .db.models import Q

class customLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pets')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('pets')
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage, self).form_valid(form)
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('pets')
        return super(RegisterPage,self).get(*args,**kwargs)        



class owner_view(ListView):
    model = owner
    context_object_name = 'owners'
    template_name = 'base/owner_list.html'
    def get_context_data(self, **kwargs) :
        
        context = super().get_context_data(**kwargs)
        #context['owners'] = context['owners'].filter(user=self.request.user)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['owners'] = context['owners'].filter(first_name__startswith=search_input)

        context['search_input'] = search_input   
        return context

    
    

class pet_view(LoginRequiredMixin,ListView):
    model = pet
    context_object_name = 'pets'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        #context['pets'] = context['pets'].filter(user=self.request.user)
        #context['count'] = context['pets'].filter(user=self.request.user) 
        search_input = self.request.GET.get('search-area') or ''
        
        if search_input:
            context['pets'] = context['pets'].filter(pet_name__startswith=search_input)
        
        context['search_input'] = search_input   
        return context
        

class pet_Detail(DetailView):
    model = pet
    context_object_name = 'pet'
    template_name = 'base/pet.html'

class owner_Detail(DetailView):
    model = owner
    context_object_name = 'owner'
    template_name = 'base/owner.html'

class ownerCreat(LoginRequiredMixin, CreateView):
    model = owner
    fields='__all__'
    def get_success_url(self):
        return reverse_lazy('owners')

class petCreat(LoginRequiredMixin, CreateView):
    model = pet
    fields='__all__'
    def get_success_url(self):
        return reverse_lazy('pets')
   

class ownerUpdate(LoginRequiredMixin, UpdateView):
    model = owner
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('owners')    

class petUpdate(LoginRequiredMixin, UpdateView):
    model = pet
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('pets')

class petDelete(LoginRequiredMixin, DeleteView):
    model = pet
    context_object_name = 'pets'
    def get_success_url(self):
        return reverse_lazy('pets')