from django.conf import settings
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse, reverse_lazy
from django.utils.text import capfirst
from django.utils.encoding import force_bytes, force_text
from django.utils import timezone
from datetime import datetime, timedelta
from apps.registry.forms.receipt import ReceiptModelForm

from apps.utils.util import empty
from ..models.receipt import Receipt


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
    model = Receipt
    template_name = 'receipt/create_form.html'

    def get_context_data(self, **kwargs):
        context = super(ReceiptCreateView, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['title'] = "Nuevo registro"
        return context



# class CarUpdateView(UpdateView):
#     model = Car
#     form_class = CarUpdateForm
#     template_name = 'car/update_form.html'

#     def get_success_url(self):
#         return reverse('car:car_detail', kwargs={'pk': self.object.pk})

#     def get_context_data(self, **kwargs):
#         context = super(CarUpdateView, self).get_context_data(**kwargs)
#         context['opts'] = self.model._meta
#         context['title'] = 'Actualizar Carro'
#         return context

#     def form_valid(self, form):
#         self.object = form.save(commit=True)
#         msg = '%(name)s "%(obj)s" fue cambiado satisfactoriamente.' % {
#             'name': capfirst(force_text(self.model._meta.verbose_name)),
#             'obj': force_text(self.object)
#         }
#         messages.success(self.request, msg)
#         return super(CarUpdateView, self).form_valid(form)


# class CarDeleteView(View):
#     success_url = reverse_lazy('car:car_list' )

#     def get(self, request, pk, *args, **kwargs):
#         Car.objects.get(id=pk).delete()
#         return HttpResponseRedirect(self.success_url)


# class CarNewContractView(View):

#     def post(self, request, *args, **kwargs):
#         from core.models.status import Status
#         car = Car.objects.get(id=request.POST.get('car'))
#         print('=>>>', car)
#         client = self.save_client(request)
#         aval = self.save_aval(request)
#         status = Status.objects.get(code_name='contract_active')
#         contract = Contract(
#             car=car,
#             client=client,
#             aval=aval,
#             status=status,
#             weeks=request.POST.get('weeks'),
#             weekly_amount=request.POST.get('weekly_amount'),
#             initial_payment_amount=request.POST.get('initial_payment_amount')
#         )
#         contract.save()
#         messages.success(request, 'Contrato registrado correctamente')
#         # return HttpResponseRedirect(reverse_lazy('car:car_list'))
#         return HttpResponseRedirect(reverse('car:car_detail', kwargs={'pk': car.id}))

#     def save_client(self, request):
#         qs = Client.objects.filter(document=request.POST.get('document'))
#         client = qs[0] if qs.exists() else Client()

#         client.document_type=request.POST.get('document_type')
#         client.document=request.POST.get('document')
#         client.first_name=request.POST.get('first_name')
#         client.last_name=request.POST.get('last_name')
#         client.email=request.POST.get('email')
#         client.phone_number=request.POST.get('phone_number')
#         client.save()
#         return client

#     def save_aval(self, request):
#         qs = Aval.objects.filter(document=request.POST.get('aval_document'))
#         aval = qs[0] if qs.exists() else Aval()
        
#         aval.document=request.POST.get('aval_document')
#         aval.first_name=request.POST.get('aval_first_name')
#         aval.last_name=request.POST.get('aval_last_name')
#         aval.email=request.POST.get('aval_email')
#         aval.phone_number=request.POST.get('aval_phone_number')
#         aval.save()
#         return aval