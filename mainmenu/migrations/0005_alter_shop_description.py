# Generated by Django 5.1.3 on 2024-11-24 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainmenu', '0004_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
