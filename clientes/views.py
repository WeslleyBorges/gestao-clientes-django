from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .forms import PessoaForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def lista_pessoas(request):
  pessoas = Pessoa.objects.all()
  return render(request, 'pessoas.html', {'pessoas': pessoas})

@login_required
def nova_pessoa(request):
  form = PessoaForm(request.POST or None, request.FILES or None)

  if form.is_valid():
    form.save()
    return redirect('lista_pessoas')

  return render(request, 'form_pessoa.html', {'form': form})

@login_required
def atualizar_pessoa(request, id):
  pessoa = get_object_or_404(Pessoa, pk=id)
  form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)

  if form.is_valid():
    form.save()
    return redirect('lista_pessoas')

  return render(request, 'form_pessoa.html', {'form': form})

@login_required
def deletar_pessoa(request, id):
  pessoa = get_object_or_404(Pessoa, pk=id)
  #form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)

  if request.method == 'POST':
    pessoa.delete()
    return redirect('lista_pessoas')

  return render(request, 'confirmacao_delete_pessoa.html', {'pessoa': pessoa})