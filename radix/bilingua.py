# radix/bilingua.py
# NuDaMu: Módulo Bilingua — Detección de idioma y respuesta base

from langdetect import detect

IDIOMAS_PERMITIDOS = ['es', 'en']

mensajes_fallback = {
    'es': "⚠️ Idioma no reconocido. Por favor escribe en español o inglés.",
    'en': "⚠️ Language not recognized. Please write in Spanish or English."
}

def detectar_idioma(texto):
    try:
        return detect(texto)
    except:
        return "desconocido"

def responder_bilingue(texto):
    idioma = detectar_idioma(texto)
    return mensajes_fallback.get(idioma, mensajes_fallback['es'])
