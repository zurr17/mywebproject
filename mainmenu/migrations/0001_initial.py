# Generated by Django 5.1.3 on 2024-11-23 15:06

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookRental',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(default='Anonymous', max_length=100)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('page', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='testimage')),
            ],
        ),
        migrations.CreateModel(
            name='Merek',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(default='', max_length=150, unique=True)),
                ('deskripsi', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(default='', max_length=150)),
                ('dekripsi', models.TextField(blank=True, default='', null=True)),
                ('stok', models.PositiveIntegerField(default=0)),
                ('harga_per_hari', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('gambar', models.ImageField(upload_to='motorimage')),
                ('merek', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainmenu.merek')),
            ],
        ),
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nik', models.CharField(max_length=15)),
                ('nama_peminjam', models.CharField(default='', max_length=150)),
                ('tanggal_pinjam', models.DateField(auto_now_add=True)),
                ('tanggal_kembali', models.DateField()),
                ('jumlah_bayar', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('sudah_bayar', models.BooleanField(default=False)),
                ('jumlah_denda', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('DIPESAN', 'Dipesan'), ('DIPINJAM', 'Dipinjam'), ('DIKEMBALIKAN', 'Dikembalikan')], default='DIPESAN', max_length=20)),
                ('motor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainmenu.motor')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewSite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(help_text='Rate 1-5', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='mainmenu.library')),
            ],
        ),
    ]
