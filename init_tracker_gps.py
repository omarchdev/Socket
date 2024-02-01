
import os
import servidorudp
import dbSqlite
import servidor
#servidor.tarea()


# inicializa la base de datos sqlite . crea hilos paralelos . cada hilo se encargara de escuchar un puerto especifico. luego de recibir los datos (trama), los guarda en la base de datos sqlite
try:

    dbSqlite.registro_db()
    servidorudp.crearHilos()
except Exception as e:
    print(e)
finally:
    while True:
        print("")
    


#servidor.tarea(13001)