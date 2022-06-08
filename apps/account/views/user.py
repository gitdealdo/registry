from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.text import capfirst
from django.utils.encoding import force_bytes, force_text
from apps.utils.util import empty
# from ..forms.user import UserModelForm

from ..models import User


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/list.html'
    paginate_by = settings.PER_PAGE

    def get_paginate_by(self, queryset):
        if 'all' in self.request.GET:
            return None
        return ListView.get_paginate_by(self, queryset)

    def get_queryset(self):
        self.o = empty(self.request, 'o', 'last_name')
        self.f = empty(self.request, 'f', 'first_name')
        self.q = empty(self.request, 'q', '')
        column_contains = u'%s__%s' % (self.f, 'contains')
        cquery = {column_contains: self.q, 'is_superuser':False}
        return self.model.objects.filter(**cquery).order_by(self.o)

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['title'] = 'Seleccione usuario para ver más detalles'
        context['o'] = self.o
        context['f'] = self.f
        context['q'] = self.q.replace('/', '-')
        return context

# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = User
#     template_name = 'user/detail.html'
# 
#     def get_context_data(self, **kwargs):
#         context = super(UserDetailView, self).get_context_data(**kwargs)
#         context['opts'] = self.model._meta
#         context['title'] = ('Detalles %s') % self.object
#         return context


class UserProfileView(LoginRequiredMixin, TemplateView):
    # model = User
    template_name = 'user/profile.html'
    # context_object_name = 'object'


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Perfecto %s!!! Tu contraseña fue actualizada correctamente' % user.username)
            return redirect('/')
        else:
            messages.error(request, 'Corrige los siguientes errores.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {'form': form})
