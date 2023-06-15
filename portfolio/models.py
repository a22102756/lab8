# models.py
from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    ects = models.PositiveIntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome

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
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ano_realizacao = models.PositiveIntegerField()
    cadeira = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    link_github = models.URLField()
    tecnologias_usadas = models.ManyToManyField(Lingua)
    competencias = models.ManyToManyField(Competencia)

    def __str__(self):
        return self.titulo


