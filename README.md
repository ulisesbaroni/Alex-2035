# 🤖 El Día de Alex — 2035
Historia interactiva con IA · Flask + Anthropic API

---

## 📁 Estructura del proyecto

```
alex2035/
├── app.py              ← Servidor Flask (backend Python)
├── requirements.txt    ← Dependencias
├── render.yaml         ← Configuración de deploy en Render
└── templates/
    └── index.html      ← Toda la UI (HTML + CSS + JS)
```

---

## 🚀 Correr localmente

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Configurar la API Key de Anthropic
```bash
# En Mac/Linux:
export ANTHROPIC_API_KEY="sk-ant-..."

# En Windows (CMD):
set ANTHROPIC_API_KEY=sk-ant-...

# En Windows (PowerShell):
$env:ANTHROPIC_API_KEY="sk-ant-..."
```

### 3. Correr el servidor
```bash
python app.py
```

Abrí el navegador en: **http://localhost:5000**

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
4. Render detecta el `render.yaml` automáticamente

### Paso 3 — Agregar la API Key
1. En el panel de Render → **Environment**
2. Agregá la variable:
   - **Key:** `ANTHROPIC_API_KEY`
   - **Value:** `sk-ant-tu-clave-aqui`
3. Click **"Save Changes"**

### Paso 4 — Deploy
Render hace el deploy automáticamente. En ~2 minutos tenés tu URL pública:
```
https://alex2035.onrender.com
```

---

## 🎮 Cómo funciona

| Escena | Decisión | Concepto IA |
|--------|----------|-------------|
| 🌅 Mañana | Organizar con/sin IA | Optimización de datos |
| 💼 Trabajo | Resolver con/sin IA | Potenciación humana |
| 🎮 Ocio | Elegir con/sin IA | Personalización |

**Finales posibles:**
- 🟢 Equilibrio humano + IA (mix de opciones)
- 🟡 Control total humano (todas opción B)
- 🔵 Dependencia digital (todas opción A)

---

## 🔑 Obtener API Key de Anthropic

1. Entrá a **https://console.anthropic.com**
2. Creá una cuenta o logueate
3. Ir a **"API Keys"** → **"Create Key"**
4. Copiá la clave (empieza con `sk-ant-`)
