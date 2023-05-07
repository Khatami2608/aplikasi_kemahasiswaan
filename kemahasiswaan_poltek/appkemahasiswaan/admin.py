from django.contrib import admin
from appkemahasiswaan.models import *

# Register your models here.
class kegiatanAdmin(admin.ModelAdmin):
	list_display = ['judul', 'tanggal_publikasi', 'Deskripsi', 'image']
	search_fields = ['judul', 'tanggal_publikasi']
	list_per_page = 5

admin.site.register(kegiatan, kegiatanAdmin)
