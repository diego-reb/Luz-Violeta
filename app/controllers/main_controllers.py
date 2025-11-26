from flask import render_template, Blueprint, session, jsonify, request
from app.extensiones import db
from app.models.Boton_panico import BotonPanico
import os
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/apoyo_psicologico')
def apoyo_psicologico():
    return render_template('psicologico.html')

@main.route('/api/chat', methods=['POST'])
def chat_api():
    data = request.json
    user_message = data.get("message")
    chat_history = data.get("history", [])

    MODEL_NAME = "gemini-2.5-flash"
    API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={os.environ.get('GEMINI_API_KEY')}"

    payload = {
        "contents": chat_history + [{"role": "user", "parts": [{"text": user_message}]}],
        "generationConfig": {"temperature": 0.7}
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        bot_reply = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        return jsonify({"reply": bot_reply})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@main.route('/boton_panico', methods=['POST'])
def presionar_boton():
    try:
        usuario_id = session.get("usuario_id") or 0  # 0 si no hay usuario
        evento = BotonPanico(usuario_id=usuario_id)
        db.session.add(evento)
        db.session.commit()
        return jsonify({"success": True, "mensaje": "Botón presionado registrado"})
    except Exception as e:
        print("Error al registrar botón:", e)
        return jsonify({"success": False, "mensaje": "Error al registrar botón"})