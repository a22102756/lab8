# Generated by Django 4.2.2 on 2023-07-16 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_remove_disciplina_professores_post_autor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='autor',
        ),
    ]
