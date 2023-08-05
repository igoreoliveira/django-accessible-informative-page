from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import base64
import io

class Page (models.Model):
    slug = models.SlugField(null=False, blank=False)
    title = models.TextField(null=False, blank=True, verbose_name='Título da página')
    style_css = models.TextField(null=False, blank=True, verbose_name='Estilo em CSS')
    def __str__(self):
        return self.slug
    
class Block(models.Model):
    title = models.TextField(null=True, blank=True, verbose_name='Título')
    subtitle = models.TextField(null=True, blank=True, verbose_name='Subtítulo')
    text = models.TextField(null=True, blank=True, verbose_name='Texto')
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="assets", null=True,blank=True, verbose_name='Imagem')
    image_alt_text = models.TextField(null=True, blank=True, verbose_name='Texto Alternativo da Imagem', help_text='Caso você tenha uma imagem no bloco, use esse campo para descrever a imagem de maneira detalhada')
    image_base64 = models.TextField(null=True, blank=True)
    #TODO: image_base64
    order = models.IntegerField(null=True, blank=True, verbose_name='Ordem', help_text='Use esse campo para ordenar os blocos')
    
    def __str__(self):
        return self.title

@receiver(post_save, sender=Page)
def convert_image_to_base64(sender, instance, **kwargs):
    for block in instance.block_set.all():
        if block.image:
            # Abre a imagem
            image = Image.open(block.image.path)
            
            # Cria um buffer em memória para guardar a imagem codificada em Base64
            buffer = io.BytesIO()
            image.save(buffer, format='PNG')
            
            # Codifica a imagem em Base64
            image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

            # Salva a representação Base64 no campo do modelo
            block.image_base64 = image_base64
            block.save()
    
