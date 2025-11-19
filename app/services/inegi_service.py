import requests
from flask import current_app

def obtener_centros_apoyo():
    api_key = current_app.config["INEGI_API_KEY"]
    url = f"https://www.inegi.org.mx/app/api/...&token={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None 