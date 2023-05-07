from django.db import models
from PIL import Image

class kegiatan(models.Model):
	judul = models.CharField(max_length=50)
	tanggal_publikasi = models.DateField()
	Deskripsi = models.TextField()
	image = models.ImageField(upload_to='covers/', null=True)

	def __str__(self):
	 	return self.judul 