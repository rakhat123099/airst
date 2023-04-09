# Generated by Django 4.1.5 on 2023-03-10 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TBLLogistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20)),
                ('order_line', models.CharField(max_length=20)),
                ('pn', models.CharField(max_length=20)),
                ('pot', models.CharField(max_length=20)),
                ('pay_terms', models.CharField(max_length=20)),
                ('delivery_terms', models.CharField(max_length=20)),
                ('delivery_date', models.DateField()),
                ('comments', models.TextField()),
                ('supplier_code', models.CharField(max_length=20)),
                ('can_edit', models.BooleanField(default=True)),
                ('pickup_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tcontract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_code', models.CharField(max_length=20)),
                ('reg_num', models.CharField(max_length=20)),
                ('pot_num', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tpickupaddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20)),
                ('e_mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tshiptoaddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='price_per_unit',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.CreateModel(
            name='Texphawb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hawb', models.CharField(max_length=20)),
                ('exp_shipping_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='da.tbllogistic')),
            ],
        ),
        migrations.AddField(
            model_name='tbllogistic',
            name='contract_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='da.tcontract'),
        ),
        migrations.AddField(
            model_name='tbllogistic',
            name='exp_hawb_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='da.texphawb'),
        ),
        migrations.AddField(
            model_name='tbllogistic',
            name='pickup_address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='da.tpickupaddress'),
        ),
        migrations.AddField(
            model_name='tbllogistic',
            name='shipto_address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='da.tshiptoaddress'),
        ),
    ]
