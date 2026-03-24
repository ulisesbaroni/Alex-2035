# 🤖 El Día de Alex — 2035
Historia interactiva con IA · Flask + Python

**Proyecto Final — Introducción a la IA | Baroni Ulises**

---

## 📁 Estructura del proyecto

```
alex2035/
├── app.py                  ← Servidor Flask (backend Python)
├── requirements.txt        ← Dependencias
├── render.yaml             ← Configuración de deploy en Render
├── README.md               ← Este archivo
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

Una historia interactiva ambientada en el año 2035 donde el usuario toma decisiones por Alex a lo largo de su día. Cada elección refleja un concepto distinto sobre el uso de la inteligencia artificial. Al final, el resultado varía según las decisiones tomadas.

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

### 1. Instalar dependencias
```bash
pip install flask gunicorn
```

### 2. Correr el servidor
```bash
python app.py
```

### 3. Abrir en el navegador
```
http://localhost:5000
```

---

## 🖼️ Agregar imágenes propias

Reemplazá las URLs de Unsplash en `templates/index.html` por rutas locales:

```html
<!-- Antes (imagen externa) -->
<img src="https://images.unsplash.com/..." >

<!-- Después (imagen propia) -->
<img src="{{ url_for('static', filename='img/tu-imagen.jpg') }}" >
```

Guardá tus imágenes en `static/img/`.

---

## 🔊 Agregar audio

Poné tu archivo de audio en:
```
static/audio/ambient.mp3
```
El audio se reproduce automáticamente al primer click del usuario y loopea en segundo plano. Se puede pausar/reanudar desde el widget en la esquina inferior derecha.

Formatos soportados: `.mp3` / `.ogg`

---

## 🌐 Deploy en Render (público en internet)

### Paso 1 — Subir a GitHub
```bash
git init
git add .
git commit -m "El día de Alex 2035"
git remote add origin https://github.com/TU_USUARIO/alex2035.git
git push -u origin main
```

### Paso 2 — Crear servicio en Render
1. Entrá a **https://render.com** y logueate con GitHub
2. Click en **"New +"** → **"Web Service"**
3. Conectá tu repositorio `alex2035`
4. Render detecta el `render.yaml` automáticamente y configura todo

### Paso 3 — Deploy
En ~2 minutos tenés tu URL pública permanente:
```
https://alex2035.onrender.com
```

> ⚠️ En el plan gratuito de Render, el servidor se duerme tras 15 minutos de inactividad. El primer acceso puede tardar ~30 segundos en despertar.

---

## 🛠️ Tecnologías utilizadas

| Herramienta | Uso |
|-------------|-----|
| Python + Flask | Servidor web y lógica del juego |
| HTML + CSS + JS | Interfaz cyberpunk (sin frameworks) |
| Gunicorn | Servidor WSGI para producción |
| Render.com | Deploy y hosting gratuito |
| Unsplash | Imágenes placeholder |
| IA generativa | Narrativa, prompts, conceptualización y código |

---

## 💡 Prompting — Concepto clave del proyecto

El proyecto incluye una sección educativa que compara prompts simples vs optimizados en tres casos:
- Organización personal
- Resolución de problemas laborales  
- Generación de imágenes con IA

**Fórmula del prompt efectivo:**
> Contexto + Rol + Objetivo + Restricciones = Resultado de calidad

---

*© 2025 | Proyecto Final — Introducción a la IA | Baroni Ulises*
