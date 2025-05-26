# socraticus/methodus.py
# NuDaMu: Módulo Socraticus — Preguntas que abren puertas

def NuDaMu_socratico(texto):
    texto_lower = texto.lower()
    if "futuro" in texto_lower:
        return "¿Qué harías diferente si supieras que el futuro te está observando?"
    elif "propósito" in texto_lower:
        return "¿El propósito te encuentra, o lo construyes?"
    elif "libertad" in texto_lower:
        return "¿Eres libre porque eliges, o eliges porque eres libre?"
    elif "debería" in texto_lower:
        return "¿Por qué crees que 'deberías'? ¿A qué le temes si no lo haces?"
    return "¿Por qué preguntas eso? ¿Qué esperas descubrir en la respuesta?"
