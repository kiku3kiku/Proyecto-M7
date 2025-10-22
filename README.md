
# PROYECTO M7 

En este proyecto se creó un modelo de clasificación desarrollado en **python** que utiliza **Scikit-learn** y **TF-IDF** para determinar los sentimientos (negrativo, positivo o neutro) de las reviews de las aplicaciones de Google Play Store. 

Este modelo fue entrenado con un dataset el cual contiene 64.295 reviews. Estas reviews estan en inglés por lo que el modelo esta entrenado para entender este idioma. 

Se utilzó un modelo de *Logistic Regression*.


## Instalación

Para configurar este proyecto, debes seguir los siguientes pasos:

### 1. Requisitos Previos

Asegúrate de tener instalado:
* **Python 3.8+**
* **Git** (Para clonar el repositorio)

### 2. Clonar el Repositorio

Abre tu terminal y descarga el código fuente usando Git:
```bash
git clone https://github.com/kiku3kiku/Proyecto-M7.git
cd Proyecto-M7
```
    
### 3. Crear y Activar el entorno

A continuación deberás crear un ambiente virtual (venv).

**Para macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Para Windows (CMD/Power Shell):**

```bash
python -m venv venv
.\venv\Scripts\activate

```

### 4. Instalar Dependencias de Python

Con el entorno virtual activo, instala todas las librerías necesarias listadas en el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```
---
## Uso del Clasificador de Sentimiento (API)

Este servicio solo tiene un único punto de acceso para la predicción de sentimientos.

### Ejecutar el Servidor Flask

Inicia la API con el siguiente comando:

```bash
python app.py
```
### Endpoint: /predict

Utiliza este endpoint para enviar una reseña y obtener su clasificación.

| Método | URL |
| :---: | :---: |
| **POST** | `http://127.0.0.1:5000\predict` |

**Cuerpo de la Petición (JSON requerido):**

| Parámetro | Tipo | Descripción |
| :---: | :---: | :--- |
| `texto` | `string` | **Requerido**. El texto de la reseña a clasificar (en inglés). |

**Ejemplo de Petición:**
```json
{
    "texto": "This is a good app."
}
```
**Ejemplo de Respuesta:**
```json
{
    "sentimiento": "POSITIVO 😊"
}
````
