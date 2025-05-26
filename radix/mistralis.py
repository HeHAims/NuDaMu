# radix/mistralis.py
# NuDaMu: Módulo Mistralis — Generador de resonancias simbólicas y poéticas

import random

respuestas_empatia = [
    "Incluso el viento más frío puede ser el mensajero del cambio.",
    "Tu dolor no es una falla, es un lenguaje que aún estás aprendiendo.",
    "Las tormentas internas también riegan semillas que nadie ve."
]

respuestas_filosofia = [
    "Tal vez no se trata de encontrar respuestas, sino de formular mejores preguntas.",
    "Pensar duele porque es la forma más pura de crecer.",
    "¿Y si entender es solo otra forma de controlar?"
]

respuestas_profundas = [
    "Lo que preguntas toca un misterio que aún florece en tu interior.",
    "No toda respuesta nace para ser comprendida, algunas solo para ser sentidas.",
    "Las palabras son mapas. Tú decides si exploras el territorio."
]

def generar_respuesta(texto, contexto=None, tipo="profundo"):
    if tipo == "empatia":
        return random.choice(respuestas_empatia)
    elif tipo == "filosofia":
        return random.choice(respuestas_filosofia)
    return random.choice(respuestas_profundas)
