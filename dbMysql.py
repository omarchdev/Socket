


import mysql.connector

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="192.99.154.9",
            port="3340",
            user="root",
            password="yellowblue1968",
            database="gpsdb"
        )
        print("Conexión exitosa a la base de datos")
        
        return conexion
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None





def insert_vehicle(array,conexion):
    try:
        conectar = conexion
        cursor = conectar.cursor()
        query = "INSERT INTO tracker_vehicle (unique_id_vehicle, data_json, date_marker) VALUES (%s, %s, %s)"
        #values = (unique_id_vehicle, data_json, date_marker)
        cursor.executemany(query, array)
        conectar.commit()
        
        return True
    except mysql.connector.Error as error:
        return False





def select_vehicle_log():
    try:
        
        conectar = conectar_bd()
        cursor = conectar.cursor()
        query = "SELECT * FROM tracker_vehicle"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as error:
        print("Error al ejecutar la consulta:", error)
        return None


