from django.shortcuts import render, redirect, get_object_or_404
from .models import Hospede
from .forms import HospedeForm
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HospedeSerializer, HospedeCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticated

@login_required
def listar_hospedes(request):
    hospedes = Hospede.objects.all()
    return render(request, 'hospedes/listar.html', {'hospedes': hospedes})

@login_required
def cadastrar_hospede(request):
    if request.method == 'POST':
        form = HospedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_hospedes')
    else:
        form = HospedeForm()
    return render(request, 'hospedes/form.html', {'form': form})

@login_required
def editar_hospede(request, cpf):
    hospede = get_object_or_404(Hospede, cpf=cpf)
    form = HospedeForm(request.POST or None, instance=hospede)
    if form.is_valid():
        form.save()
        return redirect('listar_hospedes')
    return render(request, 'hospedes/form.html', {'form': form})

@login_required
def deletar_hospede(request, cpf):
    hospede = get_object_or_404(Hospede, cpf=cpf)
    hospede.delete()
    return redirect('listar_hospedes')


class HospedeListCreateView(generics.ListCreateAPIView):
    queryset = Hospede.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return HospedeCreateUpdateSerializer
        return HospedeSerializer

class HospedeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospede.objects.all()
    lookup_field = 'cpf'   

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return HospedeCreateUpdateSerializer
        return HospedeSerializer

class HospedeListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        hospedes = Hospede.objects.all()
        serializer = HospedeSerializer(hospedes, many=True)
        return success_response("Lista de hóspedes carregada.", serializer.data)

    def post(self, request):

        serializer = HospedeCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            hospede = serializer.save()
            return success_response("Hóspede criado com sucesso.", HospedeSerializer(hospede).data, status=201)
        return error_response("Erro ao criar hóspede.", serializer.errors)