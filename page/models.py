from django.db import models

class Page (models.Model):
    slug = models.SlugField(null=False, blank=False)
    title = models.TextField(null=False, blank=True, verbose_name='Título da página')
    def __str__(self):
        return self.slug
    
    
class Block(models.Model):
    title = models.TextField(null=True, blank=True, verbose_name='Título')
    subtitle = models.TextField(null=True, blank=True, verbose_name='Subtítulo')
    text = models.TextField(null=True, blank=True, verbose_name='Texto')
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="assets", null=True,blank=True, verbose_name='Imagem')
    image_alt_text = models.TextField(null=True, blank=True, verbose_name='Texto Alternativo da Imagem', help_text='Caso você tenha uma imagem no bloco, use esse campo para descrever a imagem de maneira detalhada')
    #TODO: image_base64
    order = models.IntegerField(null=True, blank=True, verbose_name='Ordem', help_text='Use esse campo para ordenar os blocos')
    
    def __str__(self):
        return self.text
