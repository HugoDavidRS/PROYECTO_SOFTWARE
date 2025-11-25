![upsrj-logo](docs/img/upsrj.png)
# Politécnica de Santa Rosa

## Instrucciones rápidas (Instalación y ejecución)

Sigue estos pasos en PowerShell desde la raíz del proyecto para crear un entorno virtual, instalar dependencias y ejecutar la aplicación:

```powershell
# 1) Crear y activar el entorno virtual (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2) Actualizar pip e instalar dependencias
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

# 3) Ejecutar tests
python -m pytest tests/test_main.py

# 4) Ejecutar la aplicación (será accesible en http://localhost:8080)
python src/app/main.py
```

Notas:
- Si usas `cmd.exe` en vez de PowerShell, activa el entorno con `.venv\\Scripts\\activate.bat`.
- Para desarrollo es recomendable mantener el entorno virtual (`.venv`) fuera del control de versiones (ya está en `.gitignore`).
- Si vas a desplegar en producción, revisa y no subas contraseñas o credenciales en texto plano en `src/app/main.py`.

![upsrj-logo](docs/img/upsrj.png)
# Politécnica de Santa Rosa

| Subject         | Software Architectures                  |
|-----------------|-----------------------------------------|
| Title           | Final Project                           |
| Owner           | Hugo David Rosas Labra (023000694@upsrj.edu.mx) |


## Deployment URL Diagram

![alt text](docs/img/deployment.png)

## Components UML diagram

![components_uml](docs/img/components.png)



## Project Structure
```bash
OTA Sign/
│
├── src/
│   ├── app/
│   │   ├── _init_.py
│   │   ├── main.py                  # Flask entrypoint (Web Adapter)
│   │   └── routes.py                # HTTP routes
│   │
│   ├── domain/
│   │   ├── _init_.py
│   │   ├── models.py                # Entidades: BinaryFile, Signature, Approval
│   │   └── services.py              # Lógica de dominio: firmar, aprobar, validar
│   │
│   ├── application/
│   │   ├── _init_.py
│   │   ├── use_cases.py             # Casos de uso: upload, sign, approve, list
│   │   └── ports.py                 # Interfaces hacia infra (repositorios, firmas)
│   │
│   ├── infrastructure/
│   │   ├── _init_.py
│   │   ├── file_repository.py       # Guarda y recupera archivos del folder /data
│   │   ├── json_repository.py       # Simula la BD con un archivo .json
│   │   └── crypto_adapter.py        # Implementa la firma digital con cryptography
│   │
│   └── config/
│       ├── _init_.py
│       └── settings.py              # Config de entorno (dev/prod, rutas, claves)
│
├── data/
│   ├── dev_keys/
│   ├── prod_keys/
│   ├── signed/
│   └── binaries/
│
├── database.json                    # “Base de datos” local
├── requirements.txt
└── README.md