from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [

    path('', views.allCat, name = 'allCat'),
    path('muestras', views.SamplePackPage, name = 'SamplePackPage'),
    path('<slug:c_slug>', views.ProdCatDetail, name = 'ProdCatDetail'),
    path('<slug:c_slug>/<slug:product_slug>', views.SamplePack, name='SamplePack'),
    # path('<slug:c_slug>', views.allProdCat, name = 'products_by_category'),
    # path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail'),

    path('<slug:c_slug>/<slug:product_slug>/medida-y-cantidad', views.StepOneView.as_view(), name='ProdCatDetail'),
    path('<slug:c_slug>/<slug:product_slug>/subir-arte', views.StepTwoView.as_view(), name='UploadArt'),
    # path('subir-arte', views.StepTwoView.as_view(), name='UploadArt'),
]