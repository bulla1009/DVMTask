# Generated by Django 4.2.1 on 2023-05-16 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_category_options_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
