import json
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse, reverse_lazy
from ..models.person import Person

from apps.utils.util import empty
from ..models.receipt import Receipt
from ..models.service import Service
from ..models.detail import Detail


class ReciptList(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = 'receipt/list.html'

    def get_paginate_by(self, queryset):
        if 'all' in self.request.GET:
            return None
        return ListView.get_paginate_by(self, queryset)

    def get_queryset(self):
        self.paginate_by = empty(self.request, 'paginate_by', 10)
        self.o = empty(self.request, 'o', "-created_at")
        self.f = empty(self.request, 'f', 'client__cedule') 
        self.q = empty(self.request, 'q', '')
        column_contains = u'%s__%s' % (self.f, 'contains')
        query = {column_contains: self.q}
        qs = self.model.objects.filter(**query).order_by(self.o)
        return qs.select_related('client')

    def get_context_data(self, **kwargs):
        context = super(ReciptList, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['title'] = "Seleccione Registro para modificar"
        context['o'] = self.o
        context['f'] = self.f
        context['q'] = self.q
        context['paginate_by'] = self.paginate_by
        return context

 
class ReceiptDetail(LoginRequiredMixin, DetailView):
    model = Receipt
    template_name = 'receipt/detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(ReceiptDetail, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['title'] = self.object
        return context


class ReceiptCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'receipt/create_form.html'

    def get_context_data(self, **kwargs):
        context = super(ReceiptCreateView, self).get_context_data(**kwargs)
        qs_services = Service.objects.filter(is_public=True)
        context['title'] = "Nuevo comprobante"
        context['services'] = qs_services
        return context


class ReceiptSaveView(LoginRequiredMixin, View):
    success_url = reverse_lazy('registry:receipt_list' )

    def post(self, request, *args, **kwargs):
        cedule = request.POST.get('cedule')
        qs = Person.objects.filter(cedule=cedule)
        person = Person()
        if qs.exists():
            person = qs[0]
        person.cedule = cedule
        person.first_name = request.POST.get('first_name')
        person.last_name = request.POST.get('last_name')
        person.email = request.POST.get('email')
        person.cellphone = request.POST.get('cellphone')
        person.address = request.POST.get('address')
        person.save()
        
        receipt = Receipt()
        receipt.number = Receipt.objects.count() + 1
        receipt.client = person
        receipt.date = request.POST.get('date')
        receipt.total = request.POST.get('total')
        receipt.created_by = request.user.username
        receipt.save()
        
        services = json.loads(request.POST.get('servs2'))
        qs = Service.objects.filter(id__in=services)
        details = [Detail(receipt=receipt, service=d, cost=d.cost) for d in qs]
        services_extra = Service.objects.filter(is_public=False)
        for d in services_extra:
            details.append(Detail(receipt=receipt, service=d, cost=d.cost))
        Detail.objects.bulk_create(details)
        receipt.total = sum([d.cost for d in details])
        receipt.save()

        messages.success(self.request, "Comprobante creado correctamente")
        success_url = reverse('registry:receipt_detail', kwargs={'pk': receipt.pk})
        return HttpResponseRedirect(success_url)


class ReceiptDeleteView(View):
    success_url = reverse_lazy('registry:receipt_list' )

    def get(self, request, pk, *args, **kwargs):
        Receipt.objects.get(id=pk).delete()
        messages.success(request, "Comprobante eliminado correctamente")
        return HttpResponseRedirect(self.success_url)
