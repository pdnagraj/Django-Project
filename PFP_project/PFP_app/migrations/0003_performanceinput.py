# Generated by Django 4.1.7 on 2023-02-26 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PFP_app', '0002_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceInput',
            fields=[
                ('input_id', models.IntegerField(primary_key=True, serialize=False)),
                ('performance_rating', models.CharField(max_length=255)),
                ('sales_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFP_app.employee')),
            ],
        ),
    ]