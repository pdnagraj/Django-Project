# Generated by Django 4.1.7 on 2023-02-26 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PFP_app', '0003_performanceinput'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performanceinput',
            name='input_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Input ID'),
        ),
    ]
