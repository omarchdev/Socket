import threading
import datetime
import servidor

def thread_function(thread_num):
    while True:
        current_time = datetime.datetime.now()
        print(f"Hilo {thread_num}: {current_time}")

# Crea los 10 hilos
def crearHilos():
    threads = []
    for i in range(13000,13011):
        thread = threading.Thread(target=servidor.tarea, args=(i,))
        thread.start()
        threads.append(thread)

    # Espera a que todos los hilos terminen
    for thread in threads:
        thread.join()





