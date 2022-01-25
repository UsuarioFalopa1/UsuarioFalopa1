from django.db import models

# Create your models here.
class Lottery(models.Model):
   # 'id','fecha', 'letras', 'numeros', 'premios
    '''fecha = models.CharField(max_length=120, default="")
    letras = models.CharField(max_length=120, default="")
    numeros = models.CharField(max_length=120, default="")
    premios = models.CharField(max_length=120, default="")
    '''
    timestamp = models.CharField(max_length=120, default="")
    status = models.IntegerField
    numero1 = models.CharField(max_length=5, default="")
    numero2 = models.CharField(max_length=5, default="")
    numero3 = models.CharField(max_length=5, default="")
    numero4 = models.CharField(max_length=5, default="")
    numero5 = models.CharField(max_length=5, default="")
    numero6 = models.CharField(max_length=5, default="")
    numero7 = models.CharField(max_length=5, default="")
    numero8 = models.CharField(max_length=5, default="")
    numero9 = models.CharField(max_length=5, default="")
    numero10 = models.CharField(max_length=5, default="")
    numero11 = models.CharField(max_length=5, default="")
    numero12 = models.CharField(max_length=5, default="")
    numero13 = models.CharField(max_length=5, default="")
    fraseSorteoPDF = models.TextField
    fraseListaPDF = models.TextField
    listaPDF = models.TextField
    urlAudio = models.TextField
    error = models.IntegerField

    def _str_(self):
        return self.timestamp
