"""stickers_gallito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from shop import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name = 'index'),
    path('', include('shop.urls')),
    path('carrito_de_compras/', include('cart.urls')),
    path('ordenes/', include('order.urls')),
    path('marketing/', include('marketing.urls')),
    path('registrarse/', views.signupView, name = 'signup'),
    path('ingresar/', views.signinView, name = 'signin'),
    path('salir/', views.signoutView, name = 'signout'),
    path('province/', views.get_province, name = 'province')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

