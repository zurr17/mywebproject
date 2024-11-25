from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from datetime import timezone
from django.forms import BooleanField


# Create your models here.

class Library(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(
        max_length=100,
        default='Anonymous'
    )
    date = models.DateField()
    description = models.TextField()
    page = models.IntegerField(default=0)
    image = models.ImageField(upload_to='bookimage')

    def __str__(self) -> str:
        return self.title


class BookRental(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    message = models.TextField()

    def __str__(self):
        return self.name

class ReviewSite(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    comment = models.TextField(blank=True,null=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rate 1-5"
    )
    book_id = models.ForeignKey('Library',on_delete=models.CASCADE, related_name='reviews')
    def __str__(self):
        return f"{self.name} - {self.book_id.title} ({self.rating})"

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,)
    message = models.TextField()

    def __str__(self):
        return self.name

class Merek(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=150, null=False, unique=True, default="")
    deskripsi = models.TextField(default="")

    def __str__(self):
        return self.nama


class Motor(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=150, default="")
    dekripsi = models.TextField(default="",blank=True, null=True)
    merek = models.ForeignKey(Merek, on_delete=models.CASCADE, default=None)
    stok = models.PositiveIntegerField(default=0)
    harga_per_hari = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    gambar = models.ImageField(upload_to='motorimage')

    def __str__(self):
        return self.nama


class Peminjaman(models.Model):
    STATUS_CHOICES = [
        ('DIPESAN', 'Dipesan'),
        ('DIPINJAM', 'Dipinjam'),
        ('DIKEMBALIKAN', 'Dikembalikan'),
    ]

    id = models.AutoField(primary_key=True)
    nik = models.CharField(max_length=15)
    nama_peminjam = models.CharField(max_length=150, null=False, default="")
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE, default=None, null=False)
    tanggal_pinjam = models.DateField(auto_now_add=True)
    tanggal_kembali = models.DateField()
    jumlah_bayar = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    sudah_bayar = models.BooleanField(default=False)
    jumlah_denda = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='DIPESAN',
    )

    def __str__(self):
        return f"{self.nama_peminjam} - {self.motor} {self.status}"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, default="", null=False, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    description = models.TextField(default="", null=True, blank=True)
    image = models.ImageField(upload_to='products')
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Cart(object):
 def __init__(self, request):
     self.session = request.session
     cart = self.session.get(settings.CART_SESSION_ID)
     if not cart:
         # save an empty cart in the session
         cart = self.session[settings.CART_SESSION_ID] = {}
     self.cart = cart

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    cart_items = models.ManyToManyField(CartItem)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} - {self.total_cost}'