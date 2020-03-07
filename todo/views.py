from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from django.contrib.auth.views import LoginView, LogoutView

from todo.forms import CreateNotesForm, SearchBoxForm, OrderingForm
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
        search = self.request.GET.get('text')
        order = self.request.GET.get('order')
        query = Q(author=self.request.user)
        if search:
            query &= Q(text__icontains=search)
        if order in ['created_at', 'text']:
            return Notes.objects.filter(query).order_by(order)
        return Notes.objects.filter(query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {'create_form': CreateNotesForm,
             'search_form': SearchBoxForm,
             'ordering_form': OrderingForm})
        return context


class NotesSharedListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'shared.html'
    queryset = Notes.objects.filter(is_shared=True)
    paginate_by = 5


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

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        if self.request.user == self.object.author:
            self.object.delete()
        return HttpResponseRedirect(success_url)


class NoteShareView(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        pk = kwargs.get('pk')
        obj = get_object_or_404(Notes, pk=pk)
        if self.request.user == obj.author:
            obj.is_shared = not obj.is_shared
            obj.save()
        return HttpResponseRedirect(reverse_lazy('index'))
