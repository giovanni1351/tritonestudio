# Generated by Django 5.0.6 on 2025-02-28 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('release_year', models.IntegerField(blank=True, null=True, verbose_name='Ano de Lançamento')),
                ('in_development', models.BooleanField(default=False, verbose_name='Em Desenvolvimento')),
                ('details_url', models.URLField(blank=True, null=True, verbose_name='URL de Detalhes')),
                ('download_url', models.URLField(blank=True, null=True, verbose_name='URL de Download')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('order', models.IntegerField(default=0, verbose_name='Ordem de Exibição')),
            ],
            options={
                'verbose_name': 'Jogo',
                'verbose_name_plural': 'Jogos',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='GameImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='games/', verbose_name='Imagem')),
                ('alt_text', models.CharField(max_length=100, verbose_name='Texto Alternativo')),
                ('is_main', models.BooleanField(default=False, verbose_name='Imagem Principal')),
                ('order', models.IntegerField(default=0, verbose_name='Ordem')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.game')),
            ],
            options={
                'verbose_name': 'Imagem do Jogo',
                'verbose_name_plural': 'Imagens dos Jogos',
                'ordering': ['game', 'order'],
            },
        ),
    ]
