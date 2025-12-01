from datetime import date
from .models import Reserva

def verificar_reservas_vencidas():
    """
    Verifica se existem reservas cuja data de saída é ANTERIOR a hoje
    e que ainda estão marcando o quarto como ocupado.
    """
    hoje = date.today()

    # Busca reservas onde:
    # 1. Data de saída é menor que hoje (dtSaida < hoje)
    # 2. O quarto ainda está marcado como indisponível (ocupado)
    reservas_vencidas = Reserva.objects.filter(
        dtSaida__lt=hoje, 
        quarto__disponibilidade=False
    )

    count = 0
    for reserva in reservas_vencidas:
        # Libera o quarto
        quarto = reserva.quarto
        quarto.disponibilidade = True
        quarto.save()
        
        # Opcional: Se você tiver um campo status na reserva, atualize aqui
        # reserva.status = 'Finalizada' 
        # reserva.save()
        
        count += 1
    
    if count > 0:
        print(f"AUTO-CHECK: {count} reservas foram finalizadas e quartos liberados.")