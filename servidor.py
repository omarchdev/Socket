import os
import socket
import time
import dbSqlite
import textoProcesador

def establecer_conexion(puerto):
    # Crea un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlaza el socket a un puerto específico
    #  server_address = ('192.99.154.9', 13000)
    # server_address = ('192.99.154.9', puerto)
    server_address = ('127.0.0.1', puerto)   
   # server_address = ('192.99.154.9', 13000)
    sock.bind(server_address)

    # Escucha conexiones entrantes
    sock.listen(0)

    # Espera a que llegue una conexión

    #print(str(puerto)+' - Esperando una conexión...')
    connection, client_address = sock.accept()
    #print('Conexión establecida desde', client_address)
    return connection

def tarea(puerto):
    
    permite_grabar_texto=True
    
    timeout=100
    try:
        while True:
        
            connection = establecer_conexion(puerto)

            connection.settimeout(timeout)
            try:
                # Recibe los datos en trozos y reenvía la información de vuelta al cliente
                start_time = time.time()
                while True:
                    # Your code inside the loop goes here
                    connection.settimeout(timeout)
                    data = connection.recv(1024)
                    connection.settimeout(timeout)
                    if data:
                        print(data.decode())
                        # Guarda la información en un archivo de texto sin borrar lo anterior
                        tempArray = textoProcesador.dividir_texto(data.decode())
                        for textTemp in tempArray:
                            
                            permite_grabar_texto=True
                            #VALIDACIONES
                            textTemp=textTemp.replace("\n","")
                            textTemp=textTemp.replace("\r","")
                            textTemp=textTemp.replace("\t","")
                            
                            if (textTemp.strip()) =="":
                                permite_grabar_texto=False
                            if (textoProcesador.verificar_prefijo_cadena(textTemp.strip())) == False:
                                permite_grabar_texto=False
                                
                            #FIN VALIDACIONES   
                            
                            #GUARDAR EN BASE DE DATOS      
                            if permite_grabar_texto==True:
                                dbSqlite.save_marker(textTemp, time.strftime("%Y-%m-%d %H:%M:%S"))
                               # with open(str(puerto)+'-data.txt', 'a') as file:
                                #    file.write(textTemp + '\n')
                      
                               
                                    
                                    
                        #with open(str(puerto)+'-data.txt', 'a') as file:
                         #   file.write(data.decode() + '\n')
                            # analiza el texto y los separa con el simbolo $ y luego devuelve un array
                    
                         
                    else:
                       # print('No se recibieron más datos de')
                        break

            except Exception as e:
                #print('Se produjo una excepción al recibir datos. Reconectando...')
                #print(e)
                connection.close()
            finally:
                # Cierra la conexión
                #print('Cerrando la conexión')
                connection.close()
    except:
        print('Se produjo una excepción al establecer la conexión. Reconectando...')
        print("An exception occurred")


os.system('exit')

