from django.shortcuts import render
from appkemahasiswaan.models import *
from .forms import FormKegiatan
from django.contrib import messages
from django.shortcuts import render, redirect

#Menampilkan data kegiatan
def data_kegiatan(request):
    dt_kegiatan = kegiatan.objects.all()

    konteks = {
        'dt_kegiatan': dt_kegiatan,
    }
    return render(request, 'data-kegiatan.html', konteks)

#tambah kegiatan
def tambah_kegiatan(request):
	if request.POST:
		form = FormKegiatan(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			form = FormKegiatan()
			pesan = "Data Berhasil Disimpan"

			konteks = {
				'form': form,
				'pesan': pesan,
			}
			return render(request, 'tambah-kegiatan.html', konteks)

	else:
		form = FormKegiatan()

		konteks = {
			'form': form,
		}	
	return render(request, 'tambah-kegiatan.html', konteks)

#proses ubah data kegiatan
def ubah_kegiatan(request, id_kegiatan):
	dt_kegiatan = kegiatan.objects.get(id=id_kegiatan)
	template = 'ubah-kegiatan.html'
	if request.POST:
		form = FormKegiatan(request.POST, request.FILES, instance=dt_kegiatan)
		if form.is_valid():
			form.save()
			messages.success(request, 'Data Berhasil Diperbaharui!')
			return redirect('ubah_kegiatan', id_kegiatan=id_kegiatan)
	else:
		form = FormKegiatan(instance=dt_kegiatan)
		konteks = {
		    'form': form,
		    'dt_kegiatan': dt_kegiatan,
		}
	return render(request, template, konteks)

#Proses Hapus data Buku
# def hapus_kegiatan(request, id_kegiatan):
#     dlt_kegiatan = kegiatan.objects.get(id=id_kegiatan)
#     dlt_kegiatan.delete()

#     messages.success(request, 'Data Berhasil Dihapus!')
#     return redirect('data- kegiatan')

def hapus_kegiatan(request, id_kegiatan):
	dt_kegiatan = kegiatan.objects.filter(id=id_kegiatan)
	dt_kegiatan.delete()

	messages.success(request, 'Data Berhasil Dihapus!')
	return redirect('/data-kegiatan/')
