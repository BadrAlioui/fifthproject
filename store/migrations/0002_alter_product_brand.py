# Generated by Django 5.1.3 on 2024-11-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='un-branded', max_length=200),
        ),
    ]
