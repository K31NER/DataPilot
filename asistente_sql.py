import sqlite3
from openai import OpenAI
from db import get_conexion
from CONTEXTO import PROMPT_SQL
from data_processing import volver_json,obtener_datos

MODELO = "qwen2.5:1.5b"

client = OpenAI(
        base_url = 'http://localhost:11434/v1',
        api_key='ollama', # required, but unused
)

def asistente_sql(pregunta:str, modelo:str = MODELO)-> str:
    """Funcion que genera las consultas sqlite"""
    
    response = client.chat.completions.create(
        model=modelo,
        messages=[
            {"role": "assistant", "content":PROMPT_SQL},
            {"role": "user", "content":f"Pregunta: {pregunta}"}
        ]
    )
    return response.choices[0].message.content

def ejecutar_consulta(consulta: str, db_name: str = "data.sql"):
    """
    Ejecuta una consulta SQL en la base de datos especificada.

    :param consulta: Consulta SQL a ejecutar.
    :param db_name: Nombre de la base de datos SQLite.
    :return: Resultados de la consulta si es una consulta SELECT, None en caso contrario.
    """
    conexion, cursor = get_conexion(db_name)

    try:
        cursor.execute(consulta)
        conexion.commit()

        # Verificar si la consulta es un SELECT
        if consulta.strip().upper().startswith("SELECT"):
            return cursor.fetchall()

    except sqlite3.Error as e:
        print(f"Error al ejecutar consulta: {e}")
        return None

    finally:
        conexion.close()

if __name__ == "__main__":
    pregunta = input("Pregunta: ")
    respuesta = asistente_sql(pregunta.strip())
    
    json_data = volver_json(respuesta)
    sql,contexto = obtener_datos(json_data)
    
    print(f" Esta es la consulta sql: \n {sql}")
    consulta = ejecutar_consulta(sql)
    if consulta is not None:
        for fila in consulta:
            print(fila)
