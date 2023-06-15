from django.shortcuts import render
from .models import Disciplina, Lingua, Competencia, Professor, Projeto

def home_page_view(request):
    return render(request, 'portfolio/home.html')   

def blog_page_view(request):
    return render(request, 'portfolio/blog.html')

def index_page_view(request):
    return render(request, 'portfolio/index.html')

def escola_page_view(request):
    return render(request, 'portfolio/escola.html')

def disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'portfolio/disciplinas.html', {'disciplinas': disciplinas})

def linguas(request):
    linguas = Lingua.objects.all()
    return render(request, 'portfolio/linguas.html', {'linguas': linguas})

def competencias(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def professores(request):
    professores = Professor.objects.all()
    return render(request, 'portfolio/professores.html', {'professores': professores})

def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})
