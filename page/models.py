from django.db import models

class Page (models.Model):
    slug = models.SlugField(null=False,blank=False)    
    def __str__(self):
        return self.slug
    
    
class Block(models.Model):
    text = models.TextField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
