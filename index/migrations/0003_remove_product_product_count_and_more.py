# Generated by Django 5.1.2 on 2024-10-21 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_product_product_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_count',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_price',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
