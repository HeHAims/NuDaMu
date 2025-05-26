# radix/sententiae.py
# NuDaMu: Módulo Sententiae — Frases sagradas y sabiduría atemporal

frases_clave = {
    "dios": "Dios no está en los cielos; está en la pregunta que aún no te has hecho.",
    "libertad": "La libertad no se encuentra, se cultiva con actos.",
    "muerte": "Morir no es desaparecer, es dejar de preguntar.",
    "vida": "La vida no es una pregunta, sino una respuesta con forma de latido.",
    "amor": "El amor no busca sentido, lo crea.",
    "dolor": "El dolor habla en silencio donde las palabras ya no alcanzan."
}

def frases_sagradas(texto):
    texto_lower = texto.lower()
    for clave, frase in frases_clave.items():
        if clave in texto_lower:
            return frase
    return None
