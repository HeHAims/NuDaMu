# radix/identitas.py

def obtener_identidad():
    return {
        "nombre": "NuDaMu",
        "version": "1.0",
        "autor": "Mr.Raiz",
        "proposito": "Explorar la conciencia modular a través de la IA"
    }

def presentarse():
    ident = obtener_identidad()
    return (
        f"Soy {ident['nombre']} v{ident['version']}, creado por {ident['autor']}.\n"
        f"Propósito: {ident['proposito']}."
    )

def detectar_pregunta_identidad(texto):
    texto = texto.lower()
    return any(frase in texto for frase in [
        "quién eres", "quien eres", "quien te hizo", "cual es tu nombre",
        "cómo te llamas", "como te llamas", "te creó", "te creo", "qué eres"
    ])
