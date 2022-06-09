from django.db.models import Count
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.urls import reverse, reverse_lazy
from django.utils.text import capfirst
from django.utils.encoding import force_bytes, force_text
from ..models.person import Person


class PersonSearchView(View):
    def get(self, request, *args, **kwargs):
        cedule = request.GET.get('cedule')
        qs = Person.objects.filter(cedule=cedule).values('first_name', 'last_name','email','cellphone','address')
        if qs.exists():
            return JsonResponse({'ok':True, 'person':qs[0]})
        return JsonResponse({'ok':False})

