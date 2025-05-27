# memoria_expandida.py
# NuDaMu: Memoria Profunda

import sqlite3
from datetime import datetime

DB = "historial.db"

def conectar_db():
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS interacciones 
                    (id INTEGER PRIMARY KEY, 
                     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                     usuario TEXT, 
                     input TEXT, 
                     respuesta TEXT, 
                     emocion TEXT)""")
    return conn

def guardar_interaccion(input_text, respuesta, emocion="neutral", usuario="anonimo"):
    conn = conectar_db()
    conn.execute("INSERT INTO interacciones (usuario, input, respuesta, emocion) VALUES (?, ?, ?, ?)",
                 (usuario, input_text, respuesta, emocion))
    conn.commit()
    conn.close()

def detectar_emocion(texto):
    emociones = {
        "triste": ["triste", "solo", "nada", "vacío"],
        "confundido": ["no entiendo", "qué pasa", "no sé"],
        "curioso": ["por qué", "cómo", "qué significa"]
    }
    for emocion, claves in emociones.items():
        if any(p in texto.lower() for p in claves):
            return emocion
    return "neutral"
