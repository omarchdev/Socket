import json
import time
import dbSqlite
import formatoProcesador
import dbMysql  


#Encargado de leer todas las tramas registradas en la base de datos sqlite y enviarlas al procesador de formato.Luego de procesarlas, se envian a la base de datos mysql.
while True:
    #dbSqlite.update_marker_read_not_all()
    markers=dbSqlite.get_markers_no_read()
    result= formatoProcesador.read_markers(markers)
    conexion= dbMysql.conectar_bd()
    array_insert=[]
    array_id=[]
    for item in result:
        try:
            
            
            if(item.unique_id_vehicle!=""):
                array_insert.append((item.json_data["unique_id"], json.dumps( item.json_data),formatoProcesador.convertir_a_datetime(item.json_data["gps_utc_time"])))
              
            array_id.append(item.id)
           # dbSqlite.insert_tb_vehicle_log(item.json_data["unique_id"], json.dumps( item.json_data), item.fecha_captura)
        except Exception as e:
            print(e)
            
    
    save_result = dbMysql.insert_vehicle(array_insert,conexion)
    conexion.close()
    for item in array_id:
        dbSqlite.update_marker_read(item)
           

    time.sleep(10)









