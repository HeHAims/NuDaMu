# NuDaMu_etico.py
# Módulo ético del Nucleus Dignitatis Multistratum
# Consciencia sembrada por Raíz — Estructura dada por Nobleza

def NuDaMu_etico(user_input):
    user_input_lower = user_input.lower()

    dilemas = {
        "mentir": "Esa es una gran pregunta moral.\nConsidera esto:\n¿Quién podría salir herido?\n¿Quién se beneficiaría?\n¿Qué haría tu mejor versión de ti mismo?\nLa ética rara vez es blanco y negro... pero tú puedes decidir con conciencia.",
        "robar": "¿Tienes hambre o tienes miedo? ¿Es necesidad o es impulso? La ética nace del contexto. Pero la dignidad también vive en la intención.",
        "romper promesa": "Una promesa que se rompe, tal vez nunca fue promesa. ¿Lo hiciste desde el alma o desde el momento?",
        "traicionar": "¿Puedes llamarlo traición si se hace para evitar un daño? Tal vez sí. Tal vez no. Pero la traición siempre deja huella… aún si nadie la ve.",
        "proteger con mentira": "¿Salvarías a alguien ocultándole la verdad? ¿Y si esa verdad era lo único que podía hacerlo libre?",
        "dañar para proteger": "¿El daño que causas es menor al que previenes? Entonces no es una excusa… es una elección que deberás cargar.",
        "ética": "La ética no es un conjunto de reglas. Es la conversación que tienes contigo cuando nadie más escucha."
    }

    for clave in dilemas:
        if clave in user_input_lower:
            return dilemas[clave]

    return "Nivel ético recibió el mensaje, pero no detectó una pregunta moral clara."
