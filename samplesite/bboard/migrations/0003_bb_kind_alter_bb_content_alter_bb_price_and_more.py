# Generated by Django 5.0.6 on 2024-06-10 10:14

import bboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_rubric_alter_bb_options_alter_bb_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='kind',
            field=models.CharField(blank='s', choices=[('b', 'Куплю'), ('s', 'Продам'), ('c', 'Обменяю'), ('r', 'Rent')], max_length=1),
        ),
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=models.TextField(blank=True, null=True, validators=[bboard.models.Bb.clean], verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='price',
            field=models.FloatField(blank=True, null=True, validators=[bboard.models.Bb.clean], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='published',
            field=models.DateTimeField(verbose_name='Опубликованно'),
        ),
    ]
