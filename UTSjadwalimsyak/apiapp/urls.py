from django.urls import path
from . import views

app_name = 'apiapp'

urlpatterns = [
    path('',views.readJadwal_imsyak),
    path('alamat/<int:id>', views.readJadwal_imsyakiyah),
    path('buat/',views.createjadwal),
    path('edit/<int:id>', views.updatejadwal),
    path('hapus/<int:id>', views.deletejadwal),
]