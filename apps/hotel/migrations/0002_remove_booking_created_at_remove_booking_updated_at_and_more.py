# Generated by Django 4.2.5 on 2023-09-21 21:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='room',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='room',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='booking',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='hotel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='room',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='room',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='phone',
            field=models.CharField(blank=True, null=True, verbose_name='teléfono'),
        ),
    ]
