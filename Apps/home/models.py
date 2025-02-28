from django.db import models
from django.utils.text import slugify
# Create your models here.

class Reports(models.Model):
    email = models.EmailField(max_length=254,blank=False,null=False)
    name = models.CharField(max_length=254,blank=False,null=False)
    mensagem = models.TextField(blank=False, null=False)


class Game(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    release_year = models.IntegerField(verbose_name="Ano de Lançamento", blank=True, null=True)
    in_development = models.BooleanField(default=False, verbose_name="Em Desenvolvimento")
    details_url = models.URLField(verbose_name="URL de Detalhes", blank=True, null=True)
    download_url = models.URLField(verbose_name="URL de Download", blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    order = models.IntegerField(default=0, verbose_name="Ordem de Exibição")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"


class GameImage(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='games/', verbose_name="Imagem")
    alt_text = models.CharField(max_length=100, verbose_name="Texto Alternativo")
    is_main = models.BooleanField(default=False, verbose_name="Imagem Principal")
    order = models.IntegerField(default=0, verbose_name="Ordem")

    def __str__(self):
        return f"Imagem de {self.game.title} ({self.order})"

    class Meta:
        ordering = ['game', 'order']
        verbose_name = "Imagem do Jogo"
        verbose_name_plural = "Imagens dos Jogos"