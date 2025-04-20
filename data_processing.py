import re
import json

def volver_json(respuesta: str):
    # Eliminar el texto innecesario como ```json
    respuesta = respuesta.replace("```json", "").replace("```", "").strip()

    # Eliminar caracteres de control no válidos
    respuesta = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', respuesta)

    # Usar una expresión regular para extraer la parte JSON
    match = re.search(r'(\{.*\})', respuesta, re.DOTALL)

    if match:
        json_string = match.group(1)
        try:
            # Convertir la cadena JSON en un diccionario de Python
            data = json.loads(json_string)
            # Imprimir el diccionario resultante
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    print("No se pudo extraer el texto")
    return None

def obtener_datos(data:dict)->tuple:
    """ Funcion para obtener los datos claves del json"""
    
    sql = data.get("SQL", "Error: Clave 'SQL' no encontrada")
    contexto = data.get("Contexto", "Error: Clave 'Contexto' no encontrada")
    return sql,contexto   