# Generated by Django 5.0.2 on 2024-02-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_restaurant_menu_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='menu_items',
            field=models.ManyToManyField(related_name='restaurants', to='menu.menuitem'),
        ),
    ]
