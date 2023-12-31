# Generated by Django 4.2.5 on 2023-09-22 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_remove_booking_created_at_remove_booking_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Comodidad',
                'verbose_name_plural': 'Comodidades',
            },
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateTimeField(verbose_name='Inicio'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out_date',
            field=models.DateTimeField(verbose_name='Fin'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('approved', 'Aprobado'), ('outstanding', 'Pendiente')], max_length=20, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Total a Pagar'),
        ),
        migrations.AlterField(
            model_name='room',
            name='availability',
            field=models.BooleanField(default=True, verbose_name='Disponible'),
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(max_length=10, verbose_name='N° Habitación'),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=15, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='room',
            name='type',
            field=models.CharField(choices=[('individual', 'Individual'), ('doble', 'Doble'), ('suite', 'Suite')], max_length=20, verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(blank=True, to='hotel.amenity'),
        ),
    ]
