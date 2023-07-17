from django import forms
from django.forms import ModelForm
from .models import Professor, Tarefa, Post


class Professor(ModelForm):
    class Meta:
            model = Professor
            fields = '__all__'


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
        exclude = ['concluida']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }

        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }

        # o dicionário help_texts contém, para um atributo, um texto auxiliar a apresentar por baixo da janela de inserção
        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }


class PostForm(ModelForm):
    class Meta:
            model = Post
            fields = '__all__'

            widgets = {
                'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição do Post...'}),
            }

            labels = {
                'titulo': 'Título',
                'descricao': 'Descricao',
            }

            # o dicionário help_texts contém, para um atributo, um texto auxiliar a apresentar por baixo da janela de inserção
            help_texts = {
                'decricao': 'descreva o seu post',
            }

