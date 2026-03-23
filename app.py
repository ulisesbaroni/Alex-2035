from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

SCENE_RESULTS = {
    "scene1_A": "El asistente de IA analizó el calendario de Alex, sus pendientes y sus hábitos previos. En segundos organizó un cronograma optimizado, asignó prioridades y bloqueó tiempo para cada tarea. Alex comenzó el día con claridad total y sin perder un minuto en planificación.",
    "scene1_B": "Alex tardó casi 40 minutos intentando organizar su agenda manualmente. Olvidó agendar una reunión importante y subestimó el tiempo que necesitaba para una entrega. El día arrancó con desorden y una sensación de que algo siempre faltaba.",
    "scene2_A": "La IA procesó casos similares de los últimos 3 años, identificó el patrón del problema y sugirió tres soluciones ordenadas por probabilidad de éxito. Alex eligió la mejor opción y resolvió el conflicto en 20 minutos. Su jefe quedó impresionado con la velocidad y precisión.",
    "scene2_B": "Alex se sumergió en el problema sola. Revisó documentos, consultó con colegas y probó distintos enfoques. Finalmente lo resolvió, pero le llevó casi 3 horas. Llegó a la reunión de las 5pm agotada, aunque con la satisfacción de haberlo hecho por sus propios medios.",
    "scene3_A": "La IA generó una lista personalizada basada en los géneros que Alex más disfrutó el último mes, su nivel de energía actual y el tiempo disponible. Encontró una serie nueva que Alex nunca hubiera descubierto sola. La noche fue perfecta, sin dudar ni hacer scroll interminable.",
    "scene3_B": "Alex abrió todas las plataformas y estuvo 45 minutos sin poder decidir qué ver. Finalmente eligió algo al azar que resultó ser entretenido pero no excepcional. Sin embargo, en el proceso descubrió un documental que le generó curiosidad para el fin de semana.",
}

FINAL_RESULTS = {
    "equilibrio": "Alex cerró el día con una sensación de equilibrio genuino. Usó la IA cuando le sumaba valor real, y confió en su propio criterio cuando era necesario. Ese balance consciente es exactamente lo que el mundo del 2035 exige: no humanos vs máquinas, sino humanos potenciados por máquinas. El futuro no pertenece a quienes evitan la IA ni a quienes se rinden ante ella, sino a quienes aprenden a trabajar junto a ella.",
    "humano": "Alex demostró que el ser humano puede funcionar de forma autónoma incluso en 2035. Sin embargo, el costo fue real: más tiempo, más esfuerzo, más desgaste. La autonomía tiene un valor enorme, pero ignorar las herramientas disponibles no es fortaleza, es resistencia sin estrategia. En el mundo actual, elegir no usar IA también es una decisión que tiene consecuencias.",
    "dependencia": "La IA resolvió cada desafío del día de Alex con precisión y velocidad. Todo salió bien... pero Alex no tomó ninguna decisión real. No eligió, no evaluó, no pensó críticamente. En el 2035, eso es un riesgo silencioso: cuando la tecnología falla o se equivoca, Alex no tendrá las herramientas para reaccionar. La dependencia total es cómoda, hasta que deja de serlo.",
}

def calculate_ending(choices):
    ai_count = sum(1 for c in choices if c == "A")
    if ai_count == 3:
        return "dependencia"
    elif ai_count == 0:
        return "humano"
    else:
        return "equilibrio"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/scene-result", methods=["POST"])
def scene_result():
    data = request.json
    scene_key = data.get("scene_key")
    if scene_key not in SCENE_RESULTS:
        return jsonify({"error": "Escena no encontrada"}), 400
    return jsonify({"text": SCENE_RESULTS[scene_key]})

@app.route("/api/final-result", methods=["POST"])
def final_result():
    data = request.json
    choices = data.get("choices", [])
    ending_type = calculate_ending(choices)
    return jsonify({
        "ending_type": ending_type,
        "text": FINAL_RESULTS[ending_type]
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
