# DataPilot
Gestiona bases de datos SQLite sin esfuerzo con DataPilot. Este asistente IA Python (Ollama/Qwen2:1.5B) genera consultas SQL por ti, haciéndolo accesible incluso sin conocimientos avanzados.

## Descripción

DataPilot utiliza el poder del modelo de lenguaje Qwen2:1.5B a través de Ollama para interpretar las solicitudes del usuario en lenguaje natural y convertirlas en consultas SQL válidas para bases de datos SQLite. El objetivo es simplificar la interacción con bases de datos para desarrolladores, analistas o cualquier persona que necesite acceder a datos sin escribir SQL manualmente.

## Requisitos Previos

Antes de empezar, asegúrate de tener instalado lo siguiente:

1.  **Python:** Versión 3.8 o superior recomendada.
2.  **Git:** Para clonar el repositorio.
3.  **Ollama:** Sigue las instrucciones de instalación oficiales en [https://ollama.com/](https://ollama.com/).

## Instalación y Configuración

Sigue estos pasos para configurar DataPilot en tu máquina local:

1.  **Instalar Ollama:** Si aún no lo has hecho, instala Ollama desde su sitio web oficial.

2.  **Descargar y Ejecutar el Modelo LLM:**
    *   Abre tu terminal.
    *   Ejecuta el siguiente comando para descargar y poner en marcha el modelo Qwen2:1.5B. La primera vez descargará el modelo, las siguientes veces lo cargará si ya está descargado.
      ```bash
      ollama run qwen2:1.5b
      ```
    *   **¡Importante!** Deja esta terminal abierta. Ollama necesita estar ejecutando el modelo para que DataPilot pueda comunicarse con él.

3.  **Clonar el Repositorio:**
    *   Abre una **nueva** terminal (deja la de Ollama ejecutándose).
    *   Navega al directorio donde quieras guardar el proyecto.
    *   Clona el repositorio:
      ```bash
      git clone https://github.com/K31NER/DataPilot.git
      cd DataPilot 
      ```

4.  **Crear un Entorno Virtual (Recomendado):**
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

5.  **Instalar Dependencias:**
    *   Asegúrate de que tu entorno virtual está activado.
    *   Instala las librerías Python necesarias (asumiendo que tienes un archivo `requirements.txt`):
      ```bash
      pip install -r requirements.txt
      ```
      
## Cómo Usar

1.  **Asegúrate de que Ollama esté ejecutando el modelo:** Verifica que la terminal donde ejecutaste `ollama run qwen2:1.5b` siga activa y mostrando mensajes de Ollama (o esperando input).
2.  **Ejecuta DataPilot:**
    *   En la **segunda** terminal (donde clonaste el repo y activaste el entorno virtual), ejecuta el script principal de Python:
      ```bash
      python asistente-sql.py 
      ```
3.  **Interactúa:** Sigue las instrucciones que aparezcan en la terminal para realizar tus consultas a la base de datos SQLite usando lenguaje natural.

---
