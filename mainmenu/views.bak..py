# Create your views here.
# main/views.py
from lib2to3.fixes.fix_input import context
from pyexpat.errors import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Library, BookRental, ReviewSite, Motor, Peminjaman, Product, CartItem, Order
from .forms import BookRentalForm, ReviewSiteForm, ContactForm
from datetime import datetime
import locale


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for your message!")
        else:
            return render(request, 'contact.html')
    else:
        html = render(request, 'contact.html').content
        return HttpResponse(html)


def contact_thank_you(request):
    return render(request, 'contact_thank_you.html')


def library(request):
    searchTitle = request.GET.get('title')
    if searchTitle:
        books = Library.objects.filter(title__icontains=searchTitle)
    else:
        books = Library.objects.all()
    return render(request, 'library.html', {'searchTitle': searchTitle, 'books': books})


def book_rental(request):
    if request.method == 'POST':
        form = BookRentalForm(request.POST)
        if form.is_valid():
            # form.save()
            BookRental.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                message=request.POST['message'],
            )
            return redirect('book_rental')
    else:
        form = BookRentalForm()

    book_rental_entries = BookRental.objects.all()
    return render(request, 'bookrental.html', {'form': form, 'book_rental_entries': book_rental_entries})


def bookdetail(request, book_id):
    book = get_object_or_404(Library, pk=book_id)
    reviews = ReviewSite.objects.filter(book_id=book)
    # reviews = ReviewSite.objects.all()

    if request.method == 'POST':
        form = ReviewSiteForm(request.POST)

        if form.is_valid():
            name = request.POST['name'],
            comment = request.POST['comment'],
            rating = request.POST['rating'],
            ReviewSite.objects.create(
                name=(name),
                comment=comment,
                rating=int(rating[0]),
                book_id=book,
            )
            # Manual Validation
            if not name or not rating:
                return render(request, 'bookdetail.html', {
                    'book': book,
                    'comment': comment,
                    'error': 'Please fill out all fields.'
                })
            return redirect('bookdetail', book_id=book.pk)
    else:
        form = ReviewSiteForm()
        return render(request, 'bookdetail.html', {'book': book, 'form': form, 'reviews': reviews})


def motor(request):
    nama = request.GET.get('motor')
    if nama:
        motors = Motor.objects.filter(nama__icontains=nama)
    else:
        motors = Motor.objects.all()
    return render(request, 'motorhome.html', {'nama': nama, 'motors': motors})


def motordetail(request, id):
    motor = get_object_or_404(Motor, pk=id)

    pesan_berhasil = None
    jumlah_bayar = None
    durasi_peminjaman = 0

    if request.method == 'POST':
        nik = request.POST['nik']
        nama_peminjam = request.POST['nama_peminjam']
        tanggal_pinjam = datetime.strptime(request.POST['tanggal_pinjam'], "%Y-%m-%d")
        tanggal_kembali = datetime.strptime(request.POST['tanggal_kembali'], '%Y-%m-%d')

        durasi_peminjaman = (tanggal_kembali - tanggal_pinjam).days

    if durasi_peminjaman <= 0:
        pesan_berhasil = "The return date must be later than the borrowing date."
        context = {'motor': motor, 'pesan_berhasil': pesan_berhasil}
        return render(request, 'motordetail.html', context)

    jumlah_bayar = motor.harga_per_hari * durasi_peminjaman
    print(jumlah_bayar)
    locale.setlocale(locale.LC_ALL, '')
    jumlah_bayar_rupiah = locale.currency(jumlah_bayar, grouping=True, symbol=False)
    # jumlah_bayar_rupiah=0
    print(jumlah_bayar_rupiah)

    peminjaman = Peminjaman(
        nik=nik,
        nama_peminjam=nama_peminjam,
        motor=motor,
        tanggal_pinjam=tanggal_pinjam,
        tanggal_kembali=tanggal_kembali,
        jumlah_bayar=jumlah_bayar,
    )

    peminjaman.save()

    motor.stok -= 1
    motor.save()

    pesan_berhasil = f"Terimakasih telah melakukan pemesanan, silahkan datang ke tempat untuk melakukan peminjaman. Total yang harus dibayar: Rp {jumlah_bayar_rupiah}"

    context = {'motor': motor,
               'pesan_berhasil': pesan_berhasil,
               'jumlah_bayar': jumlah_bayar
               }

    return render(request, 'motordetail.html', context)

def product_list(request):
    name = request.GET.get('name')
    products = Product.objects.all()
    return render(request, 'product_list.html', {'name': name, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def cart_view(request):
    cart = request.session.get('cart', {})
    cart = self.session.get(settings.CART_SESSION_ID)
    if not cart:
        # save an empty cart in the session
        cart = self.session[settings.CART_SESSION_ID] = {}
    self.cart = cart
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart_items': cart.values(), 'total_price': total_price})
#
#
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     quantity = int(request.POST.get('quantity', 1))
#     cart_item, created = CartItem.objects.get_or_create(product=product)
#     product.stock = product.stock - quantity
#     product.save()
#     if not created:
#         cart_item.quantity += quantity
#     else:
#         cart_item.quantity = quantity
#     cart_item.save()
#     request.session.modified = True
#     print(vars(cart_item))
#     print(vars(product))
#     request.session['cart'] = {
#         'price': float(product.price),
#         'quantity': int(quantity),
#     }
#     return redirect('cart_view')
#
#
# def checkout(request):
#     return render(request, 'checkout.html')
