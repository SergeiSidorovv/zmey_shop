# Generated by Django 4.2 on 2024-02-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_goods_additional_materials_goods_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=models.TextField(max_length=5000, null=True, verbose_name='Описание товара'),
        ),
    ]
