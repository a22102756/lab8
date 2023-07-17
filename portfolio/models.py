# models.py
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    autor = models.CharField(max_length=100)
    content = models.CharField(max_length=850)
    createTime = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Lingua(models.Model):
    nome = models.CharField(max_length=100)
    criador = models.CharField(max_length=100)
    linguagens_usadas = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome 


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE, related_name='professor')

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ECTS = models.IntegerField()
    ano_letivo = models.CharField(max_length=20)
    topicos_abordados = models.CharField(max_length=300)
    professores = models.ManyToManyField(Pessoa, null=False, related_name='disciplina')

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    titulo = models.CharField(max_length=30)
    prioridade = models.IntegerField(default=1)
    concluida = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:20]

