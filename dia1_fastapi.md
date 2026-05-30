# Día 1 — Entorno y proyecto base con FastAPI

> Tiempo estimado: ~60 minutos  
> Objetivo: tener un servidor FastAPI arrancado, con la estructura de carpetas lista y el proyecto subido a GitHub.

---

## Paso 1 — Comprueba que tienes Python 3.11+

```bash
python --version
# o en algunos sistemas:
python3 --version
```

Si la versión es menor de 3.11, descárgala desde [python.org](https://python.org).

> **Windows:** puede que necesites usar `py` en vez de `python`.  
> **Mac/Linux:** usa `python3`.

---

## Paso 2 — Crea la carpeta del proyecto

```bash
mkdir trello-clone
cd trello-clone
```

---

## Paso 3 — Crea y activa el entorno virtual

```bash
python -m venv venv
```

Luego actívalo según tu sistema:

```bash
# Windows (PowerShell)
.\venv\Scripts\activate

# Windows (cmd)
venv\Scripts\activate.bat

# Mac / Linux
source venv/bin/activate
```

Sabrás que está activo porque verás `(venv)` al inicio de tu terminal.

> **Problema en Windows con PowerShell:** si ves un error de "ejecución de scripts deshabilitada", ejecuta esto primero:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

---

## Paso 4 — Instala las dependencias

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary \
    python-jose[cryptography] passlib[bcrypt] python-dotenv
```

| Librería | Para qué sirve |
|---|---|
| `fastapi` | el framework principal |
| `uvicorn` | servidor ASGI que arranca la app |
| `sqlalchemy` | ORM para hablar con la base de datos |
| `psycopg2-binary` | conector con PostgreSQL |
| `python-jose` | generar y verificar tokens JWT |
| `passlib` | hashear contraseñas de forma segura |
| `python-dotenv` | leer variables de entorno desde `.env` |

---

## Paso 5 — Guarda las dependencias

```bash
pip freeze > requirements.txt
```

Repite este comando siempre que añadas una librería nueva.

---

## Paso 6 — Crea la estructura de carpetas

```
trello-clone/
├── app/
│   ├── __init__.py       ← archivo vacío, hace que sea un módulo Python
│   ├── main.py           ← punto de entrada de la app
│   ├── database.py       ← conexión a la BD (día 2)
│   ├── models.py         ← modelos SQLAlchemy (día 2)
│   ├── schemas.py        ← schemas Pydantic (día 3)
│   └── routers/
│       └── __init__.py   ← archivo vacío
├── .env                  ← variables secretas (NO subir a git)
├── .gitignore
└── requirements.txt
```

Créalos desde la terminal:

```bash
# Mac / Linux
mkdir app app/routers
touch app/__init__.py app/main.py app/routers/__init__.py

# Windows (PowerShell)
mkdir app, app/routers
New-Item app/__init__.py, app/main.py, app/routers/__init__.py -ItemType File
```

---

## Paso 7 — Escribe tu primer endpoint

Abre `app/main.py` en tu editor (VS Code recomendado) y copia esto:

```python
from fastapi import FastAPI

app = FastAPI(
    title="Trello Clone API",
    description="API REST para gestión de tableros y tareas",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
```

---

## Paso 8 — Arranca el servidor

Desde la raíz del proyecto (donde está la carpeta `app/`):

```bash
uvicorn app.main:app --reload
```

Si ves `Uvicorn running on http://127.0.0.1:8000`, ¡está funcionando!

Abre estas URLs en el navegador:

- `http://127.0.0.1:8000` → tu endpoint raíz
- `http://127.0.0.1:8000/docs` → documentación interactiva automática ✨
- `http://127.0.0.1:8000/redoc` → documentación alternativa

> `--reload` recarga el servidor automáticamente cada vez que guardas un archivo. Solo úsalo en desarrollo.

---

## Paso 9 — Crea el .gitignore

Crea un archivo `.gitignore` en la raíz del proyecto con este contenido:

```
venv/
.env
__pycache__/
*.pyc
.DS_Store
```

---

## Paso 10 — Sube a GitHub

Crea primero un repositorio vacío en [github.com](https://github.com), luego ejecuta:

```bash
git init
git add .
git commit -m "feat: project setup with FastAPI"
git branch -M main
git remote add origin https://github.com/tuusuario/trello-clone.git
git push -u origin main
```

---

## Checklist final del día 1

Antes de cerrar, comprueba estas tres cosas:

- [ ] `/docs` carga en el navegador y muestra los endpoints
- [ ] El repositorio está en GitHub con commits visibles
- [ ] El archivo `.env` NO aparece en GitHub

---

## Siguiente paso

Mañana (día 2) conectarás la base de datos PostgreSQL y definirás los modelos `User`, `Board` y `Task` con SQLAlchemy.
