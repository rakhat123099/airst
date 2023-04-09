from django.urls import path
from . import views

urlpatterns = [
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('logistic_orders/', views.logistic_orders, name='logistic_orders'),
    path('pickup_addresses/', views.pickup_addresses, name='pickup_addresses'),
    path('shipto_addresses/', views.shipto_addresses, name='shipto_addresses'),
    path('contracts/', views.contracts, name='contracts'),
]


urlpatterns = [
    # TServiceProvider views
    path('service-providers/', views.TServiceProviderListView.as_view(), name='service-provider-list'),
    path('service-providers/create/', views.TServiceProviderCreateView.as_view(), name='service-provider-create'),
    path('service-providers/<int:pk>/update/', views.TServiceProviderUpdateView.as_view(), name='service-provider-update'),
    path('service-providers/<int:pk>/delete/', views.TServiceProviderDeleteView.as_view(), name='service-provider-delete'),

    # TInvoiceType views
    path('invoice-types/', views.TInvoiceTypeListView.as_view(), name='invoice-type-list'),
    path('invoice-types/create/', views.TInvoiceTypeCreateView.as_view(), name='invoice-type-create'),
    path('invoice-types/<int:pk>/update/', views.TInvoiceTypeUpdateView.as_view(), name='invoice-type-update'),
    path('invoice-types/<int:pk>/delete/', views.TInvoiceTypeDeleteView.as_view(), name='invoice-type-delete'),

    # TRegime views
    path('regimes/', views.TRegimeListView.as_view(), name='regime-list'),
    path('regimes/create/', views.TRegimeCreateView.as_view(), name='regime-create'),
    path('regimes/<int:pk>/update/', views.TRegimeUpdateView.as_view(), name='regime-update'),
    path('regimes/<int:pk>/delete/', views.TRegimeDeleteView.as_view(), name='regime-delete'),

    # TblInvoice views
    path('invoices/', views.TblInvoiceListView.as_view(), name='invoice-list'),
    path('invoices/create/', views.TblInvoiceCreateView.as_view(), name='invoice-create'),
    path('invoices/<int:pk>/update/', views.TblInvoiceUpdateView.as_view(), name='invoice-update'),
    path('invoices/<int:pk>/delete/', views.TblInvoiceDeleteView.as_view(), name='invoice-delete'),
    path('invoices/<int:pk>/update-shipping/', views.TblInvoiceShippingUpdateView.as_view(), name='invoice-shipping-update'),
    path('invoices/<int:pk>/delete-shipping/', views.TblInvoiceShippingDeleteView.as_view(), name='invoice-shipping-delete'),
]