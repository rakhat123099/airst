from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def client_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    orders = Order.objects.filter(client=client)
    context = {
        'client': client,
        'orders': orders
    }
    return render(request, 'client_detail.html', context)

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    status_history = order.status_set.all()
    context = {
        'order': order,
        'status_history': status_history
    }
    return render(request, 'order_detail.html', context)



def logistic_orders(request):
    orders = TBLLogistic.objects.all()
    return render(request, 'logistic_orders.html', {'orders': orders})


def pickup_addresses(request):
    addresses = Tpickupaddress.objects.all()
    return render(request, 'pickup_addresses.html', {'addresses': addresses})


def shipto_addresses(request):
    addresses = Tshiptoaddress.objects.all()
    return render(request, 'shipto_addresses.html', {'addresses': addresses})


def contracts(request):
    contracts = Tcontract.objects.all()
    return render(request, 'contracts.html', {'contracts': contracts})



class TServiceProviderListView(ListView):
    model = TServiceProvider
    template_name = 'service_provider_list.html'


class TServiceProviderCreateView(CreateView):
    model = TServiceProvider
    template_name = 'service_provider_form.html'
    fields = ['name']
    success_url = reverse_lazy('service-provider-list')


class TServiceProviderUpdateView(UpdateView):
    model = TServiceProvider
    template_name = 'service_provider_form.html'
    fields = ['name']
    success_url = reverse_lazy('service-provider-list')


class TServiceProviderDeleteView(DeleteView):
    model = TServiceProvider
    template_name = 'service_provider_confirm_delete.html'
    success_url = reverse_lazy('service-provider-list')


class TInvoiceTypeListView(ListView):
    model = TInvoiceType
    template_name = 'invoice_type_list.html'


class TInvoiceTypeCreateView(CreateView):
    model = TInvoiceType
    template_name = 'invoice_type_form.html'
    fields = ['type']
    success_url = reverse_lazy('invoice-type-list')


class TInvoiceTypeUpdateView(UpdateView):
    model = TInvoiceType
    template_name = 'invoice_type_form.html'
    fields = ['type']
    success_url = reverse_lazy('invoice-type-list')


class TInvoiceTypeDeleteView(DeleteView):
    model = TInvoiceType
    template_name = 'invoice_type_confirm_delete.html'
    success_url = reverse_lazy('invoice-type-list')


class TRegimeListView(ListView):
    model = TRegime
    template_name = 'regime_list.html'


class TRegimeCreateView(CreateView):
    model = TRegime
    template_name = 'regime_form.html'
    fields = ['code', 'is_import', 'description']
    success_url = reverse_lazy('regime-list')


class TRegimeUpdateView(UpdateView):
    model = TRegime
    template_name = 'regime_form.html'
    fields = ['code', 'is_import', 'description']
    success_url = reverse_lazy('regime-list')


class TRegimeDeleteView(DeleteView):
    model = TRegime
    template_name = 'regime_confirm_delete.html'
    success_url = reverse_lazy('regime-list')


class TblInvoiceListView(ListView):
    model = TblInvoice
    template_name = 'invoice_list.html'


class TblInvoiceCreateView(CreateView):
    model = TblInvoice
    template_name = 'invoice_form.html'
    fields = ['invoice_number', 'invoice_date', 'invoice_amount', 'pjf', 'remarks', 'invoice_type', 'service_provider', 'invoice_year']
    success_url = reverse_lazy('invoice-list')


class TblInvoiceUpdateView(UpdateView):
    model = TblInvoice
    template_name = 'invoice_form.html'
    fields = ['invoice_number', 'invoice_date', 'invoice_amount', 'pjf', 'remarks', 'invoice_type', 'service_provider', 'invoice_year']
    success_url = reverse_lazy('invoice-list')


class TblInvoiceDeleteView(DeleteView):
    model = TblInvoice
    template_name = 'invoice_confirm_delete.html'
    success_url = reverse_lazy('invoice-list')



class TblInvoiceShippingUpdateView(UpdateView):
    model = TblInvoiceShipping
    form_class = TblInvoiceShipping
    template_name = 'invoice_shipping_update.html'
    success_url = reverse_lazy('invoice_shipping_list')

class TblInvoiceShippingDeleteView(DeleteView):
    model = TblInvoiceShipping
    template_name = 'invoice_shipping_delete.html'
    success_url = reverse_lazy('invoice_shipping_list')
