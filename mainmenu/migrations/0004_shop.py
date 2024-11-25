# Generated by Django 5.1.3 on 2024-11-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainmenu', '0003_remove_bookrental_address_bookrental_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=150)),
                ('description', models.TextField(default='')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('image', models.ImageField(upload_to='shopimage')),
                ('stock', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]