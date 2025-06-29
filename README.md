# 🐾 Sistema de Gestión Veterinaria V8

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-3.2+-green.svg)
![License](https://img.shields.io/github/LICENSE/dcanosu/Sistema-Gestion-VeterinariaV8)
![Last Commit](https://img.shields.io/github/last-commit/dcanosu/Sistema-Gestion-VeterinariaV8)
![Issues](https://img.shields.io/github/issues/dcanosu/Sistema-Gestion-VeterinariaV8)
![Virtual Env](https://img.shields.io/badge/virtualenv-enabled-brightgreen)

[![Requirements](https://img.shields.io/badge/requirements-txt-yellow)](./requirements.txt)


## 🎯 Sprint 13: Funcionalidades Avanzadas para la Clínica Veterinaria

### 📌 Contexto
La clínica veterinaria ha tenido éxito en la implementación de persistencia de datos con Django ORM. Ahora desean mejorar aún más el sistema integrando funcionalidades específicas para enriquecer significativamente la interacción entre los veterinarios, el personal administrativo y los clientes. Estas funcionalidades permitirán llevar un control más detallado y profesional del cuidado de las mascotas.

## 🚀 Objetivos del Ejercicio
Cada equipo (2 a 3 estudiantes) debe extender la aplicación existente agregando las siguientes funcionalidades:

- **Gestión de medicamentos:** Crear funcionalidades para registrar, editar, listar y eliminar medicamentos disponibles en la clínica veterinaria, incluyendo campos como nombre, descripción, cantidad disponible y fecha de vencimiento.
- **Programación de cirugías veterinarias:** Registrar, visualizar, actualizar y eliminar cirugías veterinarias planificadas, vinculadas con la mascota y el veterinario responsable.
- **Registro de bitácora de consulta:** Crear un sistema que permita registrar observaciones, diagnósticos y tratamientos durante una consulta específica, vinculando cada bitácora a la mascota correspondiente.
- **Generación de historia clínica:** Implementar la posibilidad de generar dinámicamente la historia clínica completa de una mascota, utilizando como insumo todas las bitácoras asociadas a la misma.
- **Exportación de datos:** Exportar datos básicos (por ejemplo, lista de propietarios y mascotas) en formato CSV.
  
## ⚙️ Requisitos Técnicos
- Usar claramente el patrón MVT (Modelo-Vista-Plantilla) de Django.
- Integrar correctamente las nuevas funcionalidades usando Django ORM.
- Manejar adecuadamente las excepciones y registrar eventos importantes usando logging.
- Asegurar coherencia visual y estructural con la aplicación existente.
  
## 📄 Entregables
Código fuente organizado claramente en un repositorio Git.
Archivo requirements.txt actualizado con dependencias nuevas.
Archivo README.md detallando claramente cómo ejecutar y validar cada una de las funcionalidades implementadas.
Demostración en video (de máximo 10 minutos) del funcionamiento de la aplicación.

## 🧪 Instalación y Ejecución
```bash
# Clonar el repositorio
git clone https://github.com/dcanosu/Sistema-Gestion-VeterinariaV8.git
cd Sistema-Gestion-VeterinariaV8

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Ejecutar el servidor
python manage.py runserver
```

## 🖥️ Integrantes
- Daniel Cano Suárez
- Miguel Cerquera Arias
- Esteban Eusse Múnera
