from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServicosForm
from .models import Servicos_adicionais
from rest_framework import generics
from .serializers import ServicosAdicionaisCreateUpdateSerializer, ServicosAdicionaisSerializer
from rest_framework.permissions import IsAuthenticated

def criar_servico(request):
    if request.method == 'POST':
        form = ServicosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_servicos')  
    else:
        form = ServicosForm()

    return render(request, 'servicos_adicionais/form.html', {'form': form})

def editar_servico(request, id):
    servico = get_object_or_404(Servicos_adicionais, id=id)
    if request.method == 'POST':
      form = ServicosForm(request.POST, instance=servico)
      if form.is_valid():
         form.save()
         return redirect('listar_servicos')
    else:
      form = ServicosForm(instance=servico)
    return render(request, 'servicos_adicionais/form.html', {'form': form})
    
def deletar_servico(request, id):
    servico = get_object_or_404(Servicos_adicionais, id = id)
    servico.delete()
    return redirect('listar_servicos')

def listar_servicos(request):
    servico = Servicos_adicionais.objects.all()
    return render(request, 'servicos_adicionais/listar_servicos_adicionais.html', {'servicos_adicionais': servico})


class ServicosAdicionaisListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Servicos_adicionais.objects.all()
    serializer_class = ServicosAdicionaisCreateUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServicosAdicionaisSerializer
        return ServicosAdicionaisCreateUpdateSerializer


class ServicosAdicionaisRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Servicos_adicionais.objects.all()
    serializer_class = ServicosAdicionaisCreateUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServicosAdicionaisSerializer
        return ServicosAdicionaisCreateUpdateSerializer

    lookup_field = 'id'