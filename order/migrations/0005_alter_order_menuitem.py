# Generated by Django 4.2.1 on 2023-09-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
        ('order', '0004_rename_items_order_menuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='menuitem',
            field=models.ManyToManyField(related_name='menuitem', to='menu.menuitem'),
        ),
    ]
