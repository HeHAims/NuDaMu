# memoria/contextus.py
# NuDaMu: Módulo Contextus — Memoria de interacciones y estados internos

_historial = []
_estado_emocional = "neutral"

def guardar_contexto(pregunta, respuesta):
    _historial.append({"input": pregunta, "output": respuesta})

def obtener_historial():
    return _historial.copy()

def actualizar_perfil(estado_emocion):
    global _estado_emocional
    _estado_emocional = estado_emocion

def estado_actual_usuario():
    return _estado_emocional
