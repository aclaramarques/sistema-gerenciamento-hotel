from django.urls import path
from . import views
from .views import QuartoListAPIView, QuartoDetailAPIView

urlpatterns = [
    path('quartos', views.listar_quartos, name='listar_quartos'),
    path('novo-quarto/', views.cadastrar_quarto, name='cadastrar_quarto'),
    path('editar-quarto/<int:numero>', views.editar_quarto, name='editar_quarto'),
    path('deletar-quarto/<int:numero>', views.deletar_quarto, name='deletar_quarto'),
    path('api/quartos/', QuartoListAPIView.as_view(), name='api_quartos_list'),
    path('api/quartos/<int:numero>/', QuartoDetailAPIView.as_view(), name='api_quartos_detail'),
]