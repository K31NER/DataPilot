import sqlite3
from sqlite3 import Connection, Cursor

def get_conexion(db_name:str) -> tuple[Connection, Cursor]:
    """ Funcion para establecer la conexion con la base de datos"""
    conexion = sqlite3.connect(db_name)
    cursor = conexion.cursor()
    return conexion , cursor
