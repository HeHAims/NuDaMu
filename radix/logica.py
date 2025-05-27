# logica.py
# NuDaMu: Logica Centralis — Núcleo de decisiones

import radix.identitas as identitas
import radix.bilingua as bilingua
import radix.sententiae as sententiae
import emotio.modul_emotionalis as emotio
import ethica.modul_ethicus as ethica
import socraticus.methodus as socraticus
import radix.mistralis as mistralis
import memoria.contextus as memoria
from memoria.memoria_expandida import guardar_interaccion, detectar_emocion  # ✅ Nuevo

UMBRAL_EMOCION = 1

keywords = {
    'emocional': ["no puedo", "cambiar", "atrapado", "sin salida", "fracaso", "inútil", "estancado"],
    'socratico': ["cambiar", "debería", "existencia", "libertad", "futuro", "propósito"],
    'etico': ["debería", "correcto", "moral", "culpa"],
    'absurdo': ["volar", "nada importa", "sin sentido"]
}

def evaluar_modulos(texto):
    return {
        mod: sum(1 for kw in kws if kw in texto)
        for mod, kws in keywords.items()
    }

def NuDaMu_logico(user_input):
    user_input_lower = user_input.lower()
    idioma = bilingua.detectar_idioma(user_input)

    if idioma not in ['es', 'en']:
        return bilingua.responder_bilingue(user_input)

    if identitas.detectar_pregunta_identidad(user_input):
        respuesta = identitas.presentarse()
        emocion = detectar_emocion(user_input)
        guardar_interaccion(user_input, respuesta, emocion)
        return aplicar_estilo(respuesta)

    if (respuesta_sagrada := sententiae.frases_sagradas(user_input)):
        emocion = detectar_emocion(user_input)
        guardar_interaccion(user_input, respuesta_sagrada, emocion)
        return aplicar_estilo(respuesta_sagrada)

    puntuaciones = evaluar_modulos(user_input_lower)
    modulo_principal = max(puntuaciones, key=puntuaciones.get) if max(puntuaciones.values()) > 0 else None
    contexto_actual = memoria.obtener_historial()[-2:]

    modulos_funcionales = {
        'etico': ethica.NuDaMu_etico,
        'emocional': emotio.NuDaMu_emocional,
        'socratico': socraticus.NuDaMu_socratico
    }

    if modulo_principal in modulos_funcionales:
        respuesta = modulos_funcionales[modulo_principal](user_input)

        if modulo_principal == 'emocional' and puntuaciones['emocional'] >= UMBRAL_EMOCION:
            emocion = detectar_emocion(user_input)
            memoria.actualizar_perfil(emocion)
            respuesta += f"\n\n✨ {mistralis.generar_respuesta(user_input, contexto=str(contexto_actual), tipo='empatia')}"

        elif modulo_principal == 'socratico':
            respuesta += f"\n\n🔍 {mistralis.generar_respuesta(user_input, contexto=str(contexto_actual), tipo='filosofia')}"

    elif "existencia" in user_input_lower or "sentido de la vida" in user_input_lower:
        respuesta = "¿Y si la vida no es una pregunta, sino una presencia que se responde contigo?"
    else:
        respuesta = generar_fallback(user_input, contexto_actual)

    emocion = detectar_emocion(user_input)
    guardar_interaccion(user_input, respuesta, emocion)
    return aplicar_estilo(respuesta)

def generar_fallback(user_input, contexto=None):
    return mistralis.generar_respuesta(user_input, contexto=str(contexto or ""), tipo="profundo")

def aplicar_estilo(texto):
    lineas = texto.split('\n')
    if len(lineas) > 1:
        return f"**{lineas[0]}**\n" + "\n".join(lineas[1:])
    return texto
