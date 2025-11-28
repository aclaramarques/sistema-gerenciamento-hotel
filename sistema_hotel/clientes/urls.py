from django.urls import path
from . import views
from .views import HospedeListCreateView, HospedeRetrieveUpdateDeleteView

urlpatterns = [
    path('hospedes/', views.listar_hospedes, name='listar_hospedes'),
    path('novo-hospede/', views.cadastrar_hospede, name='cadastrar_hospede'),
    path('editar-hospede/<str:cpf>/', views.editar_hospede, name='editar_hospede'),
    path('deletar-hospede/<str:cpf>/', views.deletar_hospede, name='deletar_hospede'),

    path('api/hospedes/', HospedeListCreateView.as_view(), name='hospede-list-create'),
    path('api/hospedes/<str:cpf>/', HospedeRetrieveUpdateDeleteView.as_view(), name='hospede-detail'),
]
