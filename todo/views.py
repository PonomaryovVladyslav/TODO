from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView

from todo.forms import CreateNotesForm
from todo.models import Notes


class Registration(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = '/'


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'index.html'
    queryset = Notes.objects.all()
    paginate_by = 5

    def get_queryset(self):
        return Notes.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'create_form': CreateNotesForm})
        return context


class Login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')


class Logout(LoginRequiredMixin, LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request.user)
        return super().get(request, *args, **kwargs)


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    form_class = CreateNotesForm
    success_url = reverse_lazy('index')
    http_method_names = ['post', ]

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        self.object = obj.save()
        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('index')
    http_method_names = ['post', ]
    model = Notes
