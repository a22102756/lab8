from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import TarefaForm, PostForm
from .models import Post, Lingua, Competencia, Professor, Disciplina, Pessoa, Tarefa, Comment
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def activities_page_view(request):
    return render(request, 'portfolio/activities.html')


def blogueira_page_view(request):
    return render(request, 'portfolio/blogueira.html')


def web_page_view(request):
    return render(request, 'portfolio/web.html')


def news_page_view(request):
    return render(request, 'portfolio/news.html')

def index_page_view(request):
    return render(request, 'portfolio/index.html')


def escola_page_view(request):
    print("ola")
    return render(request, 'portfolio/contact.html')


def academia_page_view(request):
    disciplina = Disciplina.objects.all()
    context = {
        'disciplina': disciplina
    }
    return render(request, 'portfolio/academia.html', context)


def publication(request):
    publication = Post.objects.all()
    context = {
        'publication': publication
    }
    return render(request, 'portfolio/pubs.html', context)


def comentario(request):
    comentario = Comment.objects.all()
    context = {
        'comentario': comentario
    }
    return render(request, 'portfolio/pubs.html', context)


def post(request):
    post = Post.objects.all()
    return render(request, 'portfolio/contact.html', {post})


def linguas(request):
    linguas = Lingua.objects.all()
    return render(request, 'portfolio/contact.html', {linguas})


def competencias(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/contact.html', {competencias})


def pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'portfolio/contact.html', {pessoas})


def disciplinas(request):
    disciplina = Disciplina.objects.all()
    return render(request, 'portfolio/contact.html', disciplina)


def professores(request):
    professores = Professor.objects.all()
    if request.method == "POST":
        nome = request.POST["nome_professor"]
        email = request.POST["email_professor"]
        post = request.POST["post_professor"]
    Professor.objects.create(nome=nome, email=email, post=post)
    return HttpResponseRedirect(reverse('portfolio:escola', professores))


def Professor_view(request):
    Events = Professor.objects.all()
    context = {
        'Event': Events
    }
    return render(request=request, template_name="contact.html", context=context)


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    return render(request, "portfolio/login.html")


def login_view(request):
    print("I'm in")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:index'))
        else:
            return render(request, "portfolio/login.html", {
                'message': "Invalid credentials"
            })
    return render(request, "portfolio/login.html")


def logout_view(request):
    logout(request)
    return render(request, 'portfolio/login.html'), {
        "message": "logged out."
    }


def blogueira_page_view(request):
    context = {'tarefas': Tarefa.objects.all()}
    return render(request, 'portfolio/blogueira.html', context)


def nova_page_view(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blogueira'))

    context = {'form': form}

    return render(request, 'portfolio/nova.html')


def apaga_page_view(request, tarefa_id):
    Tarefa.objects.get(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blogueira'))


def edita_page_view(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST or None, instance=tarefa)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blogueira'))

    context = {'form': form, 'tarefa_id': tarefa_id}
    return render(request, 'portfolio/edita.html', context)


def novo_post_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blogueira'))

    context = {'form': form}

    return render(request, 'portfolio/novoPost.html')


@login_required
def edit_post_page_view(request, post_id):
    print("Mina")
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:publication'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/editPost.html', context)


def apaga_post_page_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:publication'))


def like_post(request, post_id, action):
    post = Post.objects.get(id=post_id)
    if action == 'like':
        post.likes.add(request.user)
    elif action == 'unlike':
        post.likes.remove(request.user)
    return JsonResponse({'message': 'success'})

