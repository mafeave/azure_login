"""
    Views to access microsoft graph api for user details
"""

from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings
from .forms import RegisterForm
import requests

def get_graph_token():
    """Get graph token from Microsoft Entra ID url."""
    try:
        url = settings.AD_URL

        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
        
        data = {
            'grant_type': 'client_credentials',
            'client_id': settings.CLIENT_ID,
            'client_secret': settings.CLIENT_SECRET,
            'scope': 'https://graph.microsoft.com/.default',
        }
        
        response=requests.post(url=url, headers=headers, data=data)
        json_response = response.json()
        return json_response
    except:
        return None

def login_successful(request):
    """get user details from microsoft graph apis"""
    graph_token = get_graph_token()
    
    
    try:
        if graph_token:
            url = 'https://graph.microsoft.com/v1.0/users/' + request.user.username
        
            headers={
                'Authorization':'Bearer ' + graph_token["access_token"],
                'Content-Type': 'application/json',
            }
            response = requests.get(url=url, headers=headers)
            json_response = response.json()
            print("Display Name: "+json_response["givenName"])

            return HttpResponse(f"Hola {json_response['givenName']} Login successful")
    
    except:
        return HttpResponse('Unable to fetch user details from graph APIs')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            graph_token = get_graph_token()
            if not graph_token or "access_token" not in graph_token:
                return HttpResponse("No se pudo obtener token de acceso")

            access_token = graph_token["access_token"]
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }

            email = form.cleaned_data['email']
            local_part = email.split('@')[0]

            data = {
                "accountEnabled": True,
                "displayName": f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']}",
                "givenName": form.cleaned_data['first_name'],
                "surname": form.cleaned_data['last_name'],
                "mailNickname": local_part,
                "userPrincipalName": f"{local_part}@{settings.TENANT_DOMAIN}",
                "passwordProfile": {
                    "forceChangePasswordNextSignIn": True,
                    "password": form.cleaned_data['password']
                }
            }

            response = requests.post("https://graph.microsoft.com/v1.0/users", json=data, headers=headers)
            if response.status_code == 201:
                upn = data['userPrincipalName']
                return render(request, 'register_success.html', {'upn': upn})
                #return HttpResponse("✅ Usuario creado correctamente en Microsoft Entra ID.")
            else:
                return HttpResponse(f"❌ Error al crear usuario: {response.status_code} - {response.text}")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})