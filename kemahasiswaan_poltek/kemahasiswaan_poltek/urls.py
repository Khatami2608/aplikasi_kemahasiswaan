from django.conf import settings
from django.contrib import admin
from django.urls import path
from appkemahasiswaan.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data-kegiatan/', data_kegiatan, name='data_kegiatan'),
    path('tambah-kegiatan/', tambah_kegiatan, name='tambah_kegiatan'),
    path('ubah-kegiatan/ubah/<int:id_kegiatan>/', ubah_kegiatan, name='ubah_kegiatan'),
    path('hapus-kegiatan/hapus/<int:id_kegiatan>/', hapus_kegiatan, name='hapus_kegiatan'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
