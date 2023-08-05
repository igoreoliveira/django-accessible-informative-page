# Generated by Django 4.2.3 on 2023-08-05 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_block_order_page_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='subtitle',
            field=models.TextField(blank=True, null=True, verbose_name='Subtítulo'),
        ),
        migrations.AlterField(
            model_name='block',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assets', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='block',
            name='image_alt_text',
            field=models.TextField(blank=True, help_text='Caso você tenha uma imagem no bloco, use esse campo para descrever a imagem de maneira detalhada', null=True, verbose_name='Texto Alternativo da Imagem'),
        ),
        migrations.AlterField(
            model_name='block',
            name='order',
            field=models.IntegerField(blank=True, help_text='Use esse campo para ordenar os blocos', null=True, verbose_name='Ordem'),
        ),
        migrations.AlterField(
            model_name='block',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='block',
            name='title',
            field=models.TextField(blank=True, null=True, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.TextField(blank=True, verbose_name='Título da página'),
        ),
    ]
