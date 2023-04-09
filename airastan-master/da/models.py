from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

class Order(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price_per_unit = models.DecimalField(max_digits=100, decimal_places=2)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default='Поставщик отправил заказ')

    def result(self):
        return self.quantity * self.price_per_unit
    
a = Order.objects.first()
print(a.result)

class Status(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='status_set')
    status = models.CharField(max_length=100)
    date = models.DateTimeField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.order} - {self.status}'
    



class Tpickupaddress(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    e_mail = models.EmailField()

    def __str__(self):
        return self.address


class Tshiptoaddress(models.Model):
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address


class Tcontract(models.Model):
    supplier_code = models.CharField(max_length=20)
    reg_num = models.CharField(max_length=20)
    pot_num = models.CharField(max_length=20)

    def __str__(self):
        return self.reg_num
    

class TBLLogistic(models.Model):
    order_number = models.CharField(max_length=20)
    order_line = models.CharField(max_length=20)
    pn = models.CharField(max_length=20)
    pot = models.CharField(max_length=20)
    pay_terms = models.CharField(max_length=20)
    delivery_terms = models.CharField(max_length=20)
    delivery_date = models.DateField()
    comments = models.TextField()
    contract_id = models.ForeignKey(Tcontract, on_delete=models.CASCADE)
    supplier_code = models.CharField(max_length=20)
    can_edit = models.BooleanField(default=True)
    pickup_address_id = models.ForeignKey(Tpickupaddress, on_delete=models.CASCADE)
    shipto_address_id = models.ForeignKey(Tshiptoaddress, on_delete=models.CASCADE)
    pickup_date = models.DateField()

    def __str__(self):
        return self.order_number



class TServiceProvider(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=255, db_column='NAME')

    class Meta:
        db_table = 'TSERVICEPROVIDER'


class TInvoiceType(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    type = models.CharField(max_length=255, db_column='TYPE')

    class Meta:
        db_table = 'TINVOICETYPE'


class TRegime(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    code = models.CharField(max_length=255, db_column='CODE')
    is_import = models.BooleanField(db_column='IS_IMPORT')
    description = models.CharField(max_length=255, db_column='DESCRIPTION')

    class Meta:
        db_table = 'TREGIME'


class TblInvoice(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    invoice_number = models.CharField(max_length=255, db_column='INVOICE_NUMBER')
    invoice_date = models.DateField(db_column='INVOICE_DATE')
    invoice_amount = models.DecimalField(max_digits=15, decimal_places=2, db_column='INVOICE_AMOUNT')
    pjf = models.CharField(max_length=255, db_column='PJF')
    remarks = models.CharField(max_length=255, db_column='REMARKS')
    invoice_type = models.ForeignKey(TInvoiceType, on_delete=models.PROTECT, db_column='INVOICE_TYPE_ID')
    service_provider = models.ForeignKey(TServiceProvider, on_delete=models.PROTECT, db_column='SERVICE_PROVIDER_ID')
    invoice_year = models.IntegerField(db_column='INVOICE_YEAR')

    class Meta:
        db_table = 'TBL_INVOICE'


class TblInvoiceShipping(models.Model):
    invoice = models.ForeignKey(TblInvoice, on_delete=models.CASCADE, db_column='INVOICE_ID')
    shipping = models.ForeignKey('TExpInvoiceShipping', on_delete=models.CASCADE, db_column='SHIPPING_ID')

    class Meta:
        db_table = 'TBL_INVOICE_SHIPPING'
        unique_together = ('invoice', 'shipping')


class TExpInvoice(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    invoice_number = models.CharField(max_length=255, db_column='INVOICE_NUMBER')
    invoice_date = models.DateField(db_column='INVOICE_DATE')
    amount = models.DecimalField(max_digits=15, decimal_places=2, db_column='AMOUNT')
    pjf = models.CharField(max_length=255, db_column='PJF')
    service_provider = models.ForeignKey(TServiceProvider, on_delete=models.PROTECT, db_column='SERVICE_PROVIDER_ID')
    invoice_type = models.ForeignKey(TInvoiceType, on_delete=models.PROTECT, db_column='INVOICE_TYPE_ID')
    exp_shipping = models.ForeignKey('TExpInvoiceShipping', on_delete=models.PROTECT, db_column='EXP_SHIPPING_ID')
    invoice_year = models.IntegerField(db_column='INVOICE_YEAR')

    class Meta:
        db_table = 'TEXPINVOICE'


class TExpInvoiceShipping(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    shipping_id = models.CharField(max_length=255, db_column='SHIPPING_ID')
    regime = models.ForeignKey(TRegime, on_delete=models.PROTECT, db_column='REGIME_ID')

    class Meta:
        db_table = 'TEXPINVOICE_SHIPPING'



class TCURRENCY(models.Model):
    NUM = models.CharField(max_length=3)
    CODE = models.CharField(max_length=3)
    DESCRIPTION = models.CharField(max_length=255)


class TCODE(models.Model):
    CODE_TNBD = models.CharField(max_length=255)
    DUTY = models.DecimalField(max_digits=10, decimal_places=2)
    VAT = models.DecimalField(max_digits=10, decimal_places=2)
    POSTCLEAR_ID = models.ForeignKey('TBL_POSTCLEARANCE', on_delete=models.CASCADE, related_name='codes')
    VAT_OFFSET = models.DecimalField(max_digits=10, decimal_places=2)

class TCHARACTERDEAL(models.Model):
    CODE = models.CharField(max_length=255)
    DESCRIPTION = models.CharField(max_length=255)

class TBL_POSTCLEARANCE(models.Model):
    CCD = models.CharField(max_length=255)
    STAT_COST = models.DecimalField(max_digits=10, decimal_places=2)
    PROCEDURES = models.CharField(max_length=255)
    DATE_ISSUE = models.DateField()
    DATE_SEND_ACCOUNT = models.DateField()
    FACT_COST = models.DecimalField(max_digits=10, decimal_places=2)
    VAT_TOTAL = models.DecimalField(max_digits=10, decimal_places=2)
    DUTY_TOTAL = models.DecimalField(max_digits=10, decimal_places=2)
    CURRENCY_ID = models.ForeignKey('TCURRENCY', on_delete=models.CASCADE)
    VAT_TOTAL_OFFSET = models.DecimalField(max_digits=10, decimal_places=2)
    REGIME_ID = models.ForeignKey('TREGIME', on_delete=models.CASCADE)
    CHARACTER_DEAL_ID = models.ForeignKey('TCHARACTERDEAL', on_delete=models.CASCADE)

class TBL_POSTCLEARANCE_PRECLEARANCE(models.Model):
    CODE_ID = models.ForeignKey('TCODE', on_delete=models.CASCADE)
    PRECLEARANCE_ID = models.ForeignKey('TBL_PRECLEARANCE', on_delete=models.CASCADE)

class TBL_PRECLEARANCE(models.Model):
    SHORT_DECLARATION_DATE = models.DateField()
    SHIPPING_INVOICE = models.CharField(max_length=255)
    DATE_SHIPPING_INVOICE = models.DateField()
    DATE_SEND_BC = models.DateField()
    REGIME_ID = models.ForeignKey('TREGIME', on_delete=models.CASCADE)
    REMARKS = models.TextField()

class TBL_PRECLEARANCE_SHIPPING(models.Model):
    PRECLEARANCE_ID = models.ForeignKey('TBL_PRECLEARANCE', on_delete=models.CASCADE, related_name='shippings')
    SHIPPING_ID = models.ForeignKey('TBL_SHIPPING', on_delete=models.CASCADE, default=1)
    HAWB_ID = models.ForeignKey('TBL_HAWB', on_delete=models.CASCADE, default=1)


class TBL_SHIPPING(models.Model):
    id = models.AutoField(primary_key=True)
    way_bill = models.CharField(max_length=100)
    expected_delivery = models.DateField()
    remarks = models.TextField(blank=True)
    date_transfer_docs = models.DateField(blank=True, null=True)
    act_number = models.CharField(max_length=100, blank=True)
    act_date = models.DateField(blank=True, null=True)
    act_comment = models.TextField(blank=True)


class TBL_HAWB(models.Model):
    id = models.AutoField(primary_key=True)
    shipping_id = models.ForeignKey(TBL_SHIPPING, on_delete=models.CASCADE)
    hawb = models.CharField(max_length=100)


class TexpShipping(models.Model):
    id = models.AutoField(primary_key=True)
    way_bill = models.CharField(max_length=100)
    shipping_invoice = models.CharField(max_length=100, blank=True)
    regime_id = models.ForeignKey('TRegime', on_delete=models.CASCADE)
    date_send_to_bc = models.DateField()
    date_of_placement = models.DateField(blank=True, null=True)
    declaration_num = models.CharField(max_length=100, blank=True)
    date_of_issue = models.DateField(blank=True, null=True)
    procedures = models.TextField(blank=True)
    delivery_date = models.DateField(blank=True, null=True)
    flight_number = models.CharField(max_length=100, blank=True)
    departure_date = models.DateField(blank=True, null=True)
    delay_reason = models.TextField(blank=True)


class Texphawb(models.Model):
    id = models.AutoField(primary_key=True)
    exp_shipping_id = models.ForeignKey(TexpShipping, on_delete=models.CASCADE)
    hawb = models.CharField(max_length=100)
