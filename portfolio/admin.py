from django.contrib import admin
from .models import Disciplina, Lingua, Competencia, Professor, Projeto

# Register your models here.
admin.site.register(Disciplina)
admin.site.register(Lingua)
admin.site.register(Competencia)
admin.site.register(Professor)
admin.site.register(Projeto)