# Generated by Django 3.1.6 on 2021-02-03 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Almacen', '0001_initial'),
        ('Facturacion', '0005_auto_20210203_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='CabeceraComandaModel',
            fields=[
                ('cabeceraId', models.AutoField(db_column='cabecera_id', primary_key=True, serialize=False, unique=True)),
                ('cabeceraFecha', models.DateField(db_column='cabecera_fecha', verbose_name='Fecha del pedido')),
                ('cabeceraTotal', models.DecimalField(db_column='cabecera_total', decimal_places=2, max_digits=5, verbose_name='Total del pedido')),
                ('cabeceraCliente', models.CharField(db_column='cabecera_cliente', max_length=50, verbose_name='Nombre del cliente')),
            ],
            options={
                'verbose_name': 'Comanda',
                'verbose_name_plural': 'Comandas',
                'db_table': 't_comanda_cabecera',
            },
        ),
        migrations.CreateModel(
            name='MesaModel',
            fields=[
                ('mesaId', models.AutoField(db_column='mesa_id', primary_key=True, serialize=False)),
                ('mesaNumero', models.CharField(db_column='mesa_numero', max_length=15)),
                ('mesaCapacidad', models.IntegerField(db_column='mesa_capacidad')),
                ('mesaEstado', models.BooleanField(db_column='mesa_estado', default=True)),
            ],
            options={
                'verbose_name': 'Mesa',
                'verbose_name_plural': 'Mesas',
                'db_table': 't_mesa',
            },
        ),
        migrations.CreateModel(
            name='DetalleComandaModel',
            fields=[
                ('detalleId', models.AutoField(db_column='detalle_id', primary_key=True, serialize=False)),
                ('detalleCantidad', models.IntegerField(db_column='detalle_cantidad', verbose_name='Cantidad')),
                ('detalleSubtotal', models.DecimalField(db_column='detalle_subtotal', decimal_places=2, max_digits=5, verbose_name='SubTotal inc IGV')),
                ('cabecera', models.ForeignKey(db_column='cabecera_id', on_delete=django.db.models.deletion.PROTECT, related_name='cabeceraDetalles', to='Facturacion.cabeceracomandamodel', verbose_name='Cabecera')),
                ('inventario', models.ForeignKey(db_column='inventario_id', on_delete=django.db.models.deletion.PROTECT, related_name='inventarioDetalles', to='Almacen.inventariomodel', verbose_name='Inventario')),
            ],
            options={
                'verbose_name': 'Detalle',
                'verbose_name_plural': 'Detalles',
                'db_table': 't_comanda_detalle',
            },
        ),
        migrations.CreateModel(
            name='ComprobanteModel',
            fields=[
                ('comprobanteId', models.AutoField(db_column='comprobante_id', primary_key=True, serialize=False, unique=True)),
                ('comprobanteSerie', models.CharField(db_column='comprobante_serie', max_length=4, verbose_name='Serie del comprobante')),
                ('comprobanteNumero', models.IntegerField(db_column='comprobante_numero', verbose_name='Numero del comprobante')),
                ('comprobanteTipo', models.IntegerField(db_column='comprobante_tipo', verbose_name='Tipo de Comprobante')),
                ('comprobanteCliIdentificacion', models.CharField(db_column='comprobante_identificacion', max_length=11, verbose_name='Identificacion del cliente')),
                ('comprobantePdf', models.TextField(db_column='comprobante_pdf', verbose_name='Pdf del comprobante')),
                ('comprobanteCdr', models.TextField(db_column='comprobante_cdr', verbose_name='Codigo de Respuesta del comprobante')),
                ('comprobanteXML', models.TextField(db_column='comprobante_xml', verbose_name='XML del comprobante')),
                ('cabecera', models.OneToOneField(db_column='cabecera_id', on_delete=django.db.models.deletion.CASCADE, to='Facturacion.cabeceracomandamodel', verbose_name='Comanda')),
            ],
            options={
                'verbose_name': 'Comprobante',
                'verbose_name_plural': 'Comprobantes',
                'db_table': 't_comprobante',
            },
        ),
        migrations.AddField(
            model_name='cabeceracomandamodel',
            name='mesa',
            field=models.ForeignKey(db_column='mesa_id', on_delete=django.db.models.deletion.PROTECT, related_name='mesaComandas', to='Facturacion.mesamodel', verbose_name='Mesa'),
        ),
        migrations.AddField(
            model_name='cabeceracomandamodel',
            name='usuario',
            field=models.ForeignKey(db_column='mesero_id', on_delete=django.db.models.deletion.PROTECT, related_name='usuarioComandas', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
