from django.shortcuts import render, redirect, get_object_or_404
from .forms import FuncionarioForm
from .models import Funcionario
from rest_framework import generics
from .serializers import FuncionarioSerializer, FuncionarioCreateUpdateSerializer

def criar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')  
    else:
        form = FuncionarioForm()

    return render(request, 'funcionarios/form.html', {'form': form})

def editar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    if request.method == 'POST':
      form = FuncionarioForm(request.POST, instance=funcionario)
      if form.is_valid():
         form.save()
         return redirect('listar_funcionarios')
    else:
      form = FuncionarioForm(instance=funcionario)
    return render(request, 'funcionarios/form.html', {'form': form})
    

def deletar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id = id)
    funcionario.delete()
    return redirect('listar_funcionarios')

def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios/listar_funcionarios.html', {'funcionarios': funcionarios})


class FuncionarioListCreateView(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return FuncionarioCreateUpdateSerializer
        return FuncionarioSerializer


class FuncionarioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return FuncionarioCreateUpdateSerializer
        return FuncionarioSerializer