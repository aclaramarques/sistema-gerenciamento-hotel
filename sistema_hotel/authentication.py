# sistema_hotel/authentication.py

import os
import firebase_admin
from firebase_admin import auth, credentials
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

# Inicializa o Firebase Admin SDK se ainda não estiver iniciado
if not firebase_admin._apps:
    try:
        # Caminho para o arquivo que você baixou
        cred_path = os.path.join(settings.BASE_DIR, 'firebase_credentials.json')
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    except Exception as e:
        # Se der erro ao carregar o arquivo, imprime no console para ajudar a debugar
        print(f"ERRO AO CARREGAR FIREBASE CREDENTIALS: {e}")
        # Não damos raise aqui para não quebrar o runserver se o arquivo não existir ainda,
        # mas a autenticação vai falhar se tentarem usar.

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Pega o cabeçalho Authorization
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None

        # Separa "Bearer" do "Token"
        parts = auth_header.split()
        if parts[0].lower() != 'bearer':
            return None

        if len(parts) == 1:
            raise exceptions.AuthenticationFailed('Cabeçalho de Token inválido. Credenciais não fornecidas.')
        elif len(parts) > 2:
            raise exceptions.AuthenticationFailed('Cabeçalho de Token inválido. Espaços não permitidos.')

        token = parts[1]

        try:
            # 1. Verifica o token com o Firebase (Google)
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            email = decoded_token.get('email', '')

        except Exception as e:
            # Dica: Imprima o erro para ajudar no debug
            print(f"Erro validação Firebase: {e}")
            raise exceptions.AuthenticationFailed('Token Firebase inválido ou expirado.')

        # 2. Busca ou Cria o usuário no Django
        try:
            # Tenta achar pelo username (usamos o UID do Firebase como username)
            user = User.objects.get(username=uid)
        except User.DoesNotExist:
            # Se não existe, cria um usuário Django automaticamente
            user = User.objects.create_user(username=uid, email=email)
            user.set_unusable_password() # Não tem senha, só entra via token
            user.save()

        return (user, None)