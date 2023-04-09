from django.contrib import admin
from .models import *

admin.site.register(Order)
admin.site.register(Client)
admin.site.register(Status)

admin.site.register(TBLLogistic)
admin.site.register(Tpickupaddress)
admin.site.register(Tshiptoaddress)
admin.site.register(Tcontract)


admin.site.register(TServiceProvider)
admin.site.register(TInvoiceType)
admin.site.register(TRegime)
admin.site.register(TblInvoice)
admin.site.register(TblInvoiceShipping)
admin.site.register(TExpInvoice)
admin.site.register(TExpInvoiceShipping)


admin.site.register(TCURRENCY)
admin.site.register(TCODE)
admin.site.register(TCHARACTERDEAL)
admin.site.register(TBL_POSTCLEARANCE)
admin.site.register(TBL_POSTCLEARANCE_PRECLEARANCE)
admin.site.register(TBL_PRECLEARANCE)
admin.site.register(TBL_PRECLEARANCE_SHIPPING)

admin.site.register(TBL_SHIPPING)
admin.site.register(TBL_HAWB)
admin.site.register(TexpShipping)
admin.site.register(Texphawb)
