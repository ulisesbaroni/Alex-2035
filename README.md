# 🤖 El Día de Alex — 2035
Historia interactiva con IA · Flask + Python

**Proyecto Final — Introducción a la IA | Baroni Ulises**

🌐 **Demo en vivo:** https://alex-2035.onrender.com

---

## 📁 Estructura del proyecto

```
alex2035/
├── app.py                  ← Servidor Flask (backend Python)
├── requirements.txt        ← Dependencias
├── render.yaml             ← Configuración de deploy en Render
├── templates/
│   └── index.html          ← Toda la UI (HTML + CSS + JS)
└── static/
    ├── audio/
    │   └── ambient.mp3     ← Audio ambient en loop
    └── img/
        └── *.jpg / *.png   ← Imágenes de cada escena
```

---

## 🎮 Concepto

Historia interactiva ambientada en el año 2035 donde el usuario toma decisiones por Alex a lo largo de su día. Cada elección refleja un concepto distinto sobre el uso de la inteligencia artificial.

**Escenas:**
| # | Escena | Tema |
|---|--------|------|
| 1 | 🌅 Mañana | Organización con/sin IA |
| 2 | 💼 Trabajo | Resolución de problemas |
| 3 | 🎮 Ocio | Personalización y recomendación |
| 4 | 🔧 Prompting | Cómo comunicarse con la IA |

**Finales posibles:**
| Elecciones | Final |
|------------|-------|
| Mayoría con IA | 🟢 Equilibrio humano + IA |
| Todas sin IA | 🟡 Control total humano |
| Todas con IA | 🔵 Dependencia digital |

---

## 🚀 Correr localmente

```bash
pip install flask gunicorn
python app.py
# → http://localhost:5000
```

---

## 🛠️ Tecnologías utilizadas

| Herramienta | Uso |
|-------------|-----|
| Python + Flask | Servidor web y lógica del juego |
| HTML + CSS + JS | Interfaz cyberpunk (sin frameworks) |
| Gunicorn | Servidor WSGI para producción |
| Render.com | Deploy y hosting |
| IA generativa | Narrativa, prompts, conceptualización y código |

---

## 💡 Fórmula del prompt efectivo

> Contexto + Rol + Objetivo + Restricciones = Resultado de calidad

---

*© 2025 | Proyecto Final — Introducción a la IA | Baroni Ulises*
