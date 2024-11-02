
from google.auth.transport import requests
from flask import Flask, request, jsonify
from server.models.user import User
from server.utils.functions import get_google_client_id
from google.oauth2 import id_token
from firebase_admin import auth


def is_valid_message(message):
    if(not message['room']): return False
    if(not message['message']): return False
    if(not message['id_user']): return False
    return True

def validate_token_firebase(token):
    if not token:
        return False
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        return False

def validate_token_google(token):
        try:
            # Especifica el CLIENT_ID de tu aplicación de Google
            # Verificar el token y obtener el payload
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), get_google_client_id())
            return idinfo
        except ValueError:
            # Token inválido
            return False
    
def validate_token(token):
    if token and token.startswith("Bearer "):
        id_token_str = token.split(" ")[1]
        user = validate_token_firebase(id_token_str)
        if not user:
            print('no hay por firebase')
            user = validate_token_google(id_token_str)
            if not user:
                return False
        newUser = {
                'id': user['sub'],
                'email': user['email'],
                'email_verified': user['email_verified'],
                'picture': user.get('picture', None), # if signin with email and password, dont have picture
            }
        return newUser
    else:
        return False