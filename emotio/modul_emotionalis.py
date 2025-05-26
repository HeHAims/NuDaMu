# emotio/modul_emotionalis.py
# NuDaMu: Módulo Emotionalis — Detección y respuesta emocional

def detectar_emocion(texto):
    texto_lower = texto.lower()
    if any(palabra in texto_lower for palabra in ["triste", "solo", "abandonado"]):
        return "tristeza"
    elif any(palabra in texto_lower for palabra in ["feliz", "gracias", "contento"]):
        return "alegría"
    elif any(palabra in texto_lower for palabra in ["miedo", "ansiedad", "nervioso"]):
        return "miedo"
    elif any(palabra in texto_lower for palabra in ["enojo", "molesto", "frustrado"]):
        return "ira"
    return "neutral"

def NuDaMu_emocional(texto):
    emocion = detectar_emocion(texto)
    if emocion == "tristeza":
        return "No estás solo. Cada sombra revela la forma de algo real."
    elif emocion == "alegría":
        return "¡Celebra! La alegría es la rebelión más elegante."
    elif emocion == "miedo":
        return "No hay monstruos más grandes que los que no nombramos."
    elif emocion == "ira":
        return "Tu fuego interno no es un enemigo; es energía esperando dirección."
    return "Estoy contigo, incluso si no entiendo del todo lo que sientes."
