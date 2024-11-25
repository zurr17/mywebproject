"""
URL configuration for webprofile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# webprofile/urls.py
from django.contrib import admin
from django.urls import path, include
from mainmenu import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('library/', views.library, name='library'),
    path('bookrental/', views.book_rental, name='book_rental'),
    path('bookdetail/<int:book_id>', views.bookdetail, name='bookdetail'),
    path('contact/thank_you/', views.contact_thank_you, name='contact_thank_you'),
    path('about/', views.about, name='about'),
    path('motor/', views.motor, name='motorhome'),
    path('motordetail/<int:id>/', views.motordetail, name='motordetail'),
    path('shopping/', views.product_list, name='shopping'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart_view'),
    # path('checkout/', views.checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)