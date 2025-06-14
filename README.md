# Registro y Autenticación con Microsoft Entra ID en Django

Este proyecto está desarrollado en **Python** usando el framework **Django**, e implementa:

- Registro de usuarios a través de un formulario personalizado
- Creación de usuarios directamente en **Microsoft Entra ID** (Azure Active Directory), usando **Microsoft Graph API**
- Autenticación de usuarios con Microsoft Entra ID usando `django-auth-adfs`
- Estilizado moderno con **Tailwind CSS**
- Modal de confirmación con redirección automática

---

## 🚀 Requisitos

### Lenguaje y Framework

- Python 3.10+
- Django 4.x


## Configuración del entorno

1. Clonar el repositorio del Root: 

    ```bash
    git clone https://github.com/mafeave/azure_login.git
    cd azure_login
    ```

2. Crea un entorno virtual:

    ```bash
    python -m venv env
    source env/bin/activate  # Linux/macOS
    env\Scripts\activate     # Windows
    ```
    
3. Instala las dependencias con:
   
    ```bash
    pip install -r requirements.txt
    ```
    o manualmente 
    ```bash
    pip install django requests django-auth-adfs python-dotenv
    ```

4. Variables de entorno
    Crear un archivo .env en la raíz del proyecto con las siguientes variables:
    ```bash
    CLIENT_ID=tu_client_id
    CLIENT_SECRET=tu_client_secret
    TENANT_ID=tu_tenant_id
    TENANT_DOMAIN=midominio.onmicrosoft.com
    ```

    Client ID:
   
    <img width="710" alt="Client ID" src="https://github.com/user-attachments/assets/aed178fa-6c43-462b-9cc3-49927f4aed98" />

    CLIENT_SECRET:
   
    <img width="729" alt="client_secret" src="https://github.com/user-attachments/assets/1528f071-81b6-4443-87a6-2317baf39130" />

    TENANT ID and DOMAIN:
   
    <img width="751" alt="tenant" src="https://github.com/user-attachments/assets/8211aabf-6735-4a69-a36f-73f007370a96" />


6. Aplicar migraciones y correr el servidor:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

    Para que corra localmente por HTTPS:
    ```bash
    python manage.py runserver_plus --cert-file cert.pem
    ```
