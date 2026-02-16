from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Vagas
from .forms import dadosVagas, avaliacaoRH

def is_rh(user):
    return user.is_staff or user.groups.filter(name="RH").exists()

def login_rh(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('painel_rh')
        messages.error(request, "Usuário ou senha inválidos.")
    return render(request, 'vagasAbertas/login_rh.html')

def criar_vaga(request):
    if request.method == "POST":
        form = dadosVagas(request.POST)
        if form.is_valid():
            vaga = form.save(commit=False)
            vaga.solicitante = request.user if request.user.is_authenticated else None
            vaga.save()
            messages.success(request, "Vaga criada com sucesso! O RH entrará em contato")
            return redirect("criar_vaga")
    else:
        form = dadosVagas()
    return render(request, "vagasAbertas/criar_vaga.html", {"form": form})

@login_required
def editar_vaga(request, vaga_id):
    vaga = get_object_or_404(Vagas, id=vaga_id)
    if not is_rh(request.user):
        messages.error(request, "Você não ter permissão para editar esta vaga.")
        return redirect("listar_vagas")
    
    form = dadosVagas(request.POST or None, instance = vaga)
    if form.is_valid():
        form.save()
        messages.success(request, "Vaga atualizada com sucesso!")
        return redirect("listar_vagas" if vaga.solicitante == request.user else "listar_vagas")
    return render(request, "vagasAbertas/editar_vaga.html", {"form": form, "vaga": vaga})

@login_required
@user_passes_test(is_rh)
def excluir_vaga(request, vaga_id):
    vaga = get_object_or_404(Vagas, id=vaga_id)
    if request.method == "POST":
        vaga.delete()
        messages.success(request, "Vaga excluída com sucesso!")
        return redirect("painel_rh")
    return render(request, "vagasAbertas/excluir_vaga.html", {"vaga":vaga})

@login_required
@user_passes_test(is_rh)
def painel_rh(request):
    return redirect("listar_vagas")

@login_required
@user_passes_test(is_rh)
def listar_vagas(request):
    status = request.GET.get("status")
    vagas = Vagas.objects.all().order_by('-data_cadastro')
    if status:
        vagas = vagas.filter(status=status)
    return render(request, "vagasAbertas/listar_vagas.html", {"vagas":vagas, "filtro_status":status})

@login_required
@user_passes_test(is_rh)
def avaliar_vaga(request, vaga_id):
    vaga = get_object_or_404(Vagas, id=vaga_id)
    
    if request.method == "POST":
        acao = request.POST.get('acao')
        form = avaliacaoRH(request.POST, instance=vaga)
        
        if acao == "aprovar":
            vaga.status = "aprovado"
            vaga.save()
            messages.success(request, "Vaga aprovada com sucesso!")
            return redirect("painel_rh")
        
        elif acao == "rejeitar":
            vaga.status = "rejeitar"
            vaga.save()
            vaga.delete()
            messages.success(request, "Vaga rejeitada com sucesso!")
            return redirect("painel_rh")
        
        if form.is_valid():
            form.save()
            messages.success(request, "Avaliação registrada com sucesso!")
            return redirect("painel_rh")
    else:
        form = avaliacaoRH(instance=vaga)    
    
    return render(request, "vagasAbertas/avaliar_vaga.html", {"form": form, "vaga": vaga})
    
@login_required
@user_passes_test(is_rh)
def aprovar_vaga(request, vaga_id):
    vaga = get_object_or_404(Vagas, id=vaga_id)
    vaga.status = "aprovado"
    vaga.ativa = True
    vaga.save()
    messages.success(request, "Vaga aprovada")
    return redirect("listar_vagas")


@login_required
@user_passes_test(is_rh)
def rejeitar_vaga(request, vaga_id):
    vaga = get_object_or_404(Vagas, id=vaga_id)
    vaga.status = "rejeitado"
    vaga.ativa = False
    vaga.save()
    messages.success(request, "Vaga rejeitada.")
    return redirect("listar_vagas")

@login_required
@user_passes_test(is_rh)
def ativar_vaga(request, vaga_id):
    vaga = get_object_or_404(Vagas, id=vaga_id)
    vaga.ativa = True
    vaga.save()
    messages.success(request, "Vaga ativada.")
    return redirect("listar_vagas")

@login_required
@user_passes_test(is_rh)
def desativar_vaga(request, vaga_id):
    vaga = get_object_or_404(Vagas, id=vaga_id)
    vaga.ativa = False
    vaga.save()
    messages.success(request, "Vaga desativada.")
    return redirect("listar_vagas")