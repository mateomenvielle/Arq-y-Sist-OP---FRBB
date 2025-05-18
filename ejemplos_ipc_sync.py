from multiprocessing import Process, Queue, Lock
import time  # Usado si queremos simular demoras

# -------------------------------
# Ejemplo 1: Comunicación entre procesos con Queue (IPC)
# -------------------------------

# Proceso que actúa como "productor": pone un mensaje en la cola
def productor(q):
    q.put("Mensaje desde el productor")  # Envia un mensaje a la cola

# Proceso que actúa como "consumidor": toma un mensaje de la cola
def consumidor(q):
    mensaje = q.get()  # Espera (bloquea) hasta que haya un mensaje
    print("Consumidor recibió:", mensaje)

# Función para ejecutar el ejemplo de comunicación con Queue
def ejemplo_ipc():
    q = Queue()  # Creamos la cola de comunicación
    p1 = Process(target=productor, args=(q,))    # Proceso productor
    p2 = Process(target=consumidor, args=(q,))   # Proceso consumidor
    p1.start()  # Inicia el productor
    p2.start()  # Inicia el consumidor
    p1.join()   # Espera a que termine el productor
    p2.join()   # Espera a que termine el consumidor

# -------------------------------
# Ejemplo 2: Sincronización con Lock
# -------------------------------

# Función que simula el acceso a un recurso compartido
def tarea(nombre, lock):
    lock.acquire()  # Solicita acceso exclusivo (zona crítica)
    try:
        print(f"{nombre} accede al recurso")
        # time.sleep(2)  # Descomentar para simular una tarea larga
    finally:
        lock.release()  # Libera el recurso para que otro proceso lo use

# Función para ejecutar el ejemplo de sincronización
def ejemplo_sync():
    lock = Lock()  # Creamos el "candado" (lock)
    p1 = Process(target=tarea, args=("Proceso 1", lock))  # Primer proceso
    p2 = Process(target=tarea, args=("Proceso 2", lock))  # Segundo proceso
    p1.start()  # Inicia Proceso 1
    p2.start()  # Inicia Proceso 2
    p1.join()   # Espera que Proceso 1 termine
    p2.join()   # Espera que Proceso 2 termine

# -------------------------------
# Código principal: se ejecuta si el archivo es ejecutado directamente
# -------------------------------
if __name__ == '__main__':
    print("== Ejemplo de Comunicación entre procesos ==")
    ejemplo_ipc()

    print("\n== Ejemplo de Sincronización con Lock ==")
    ejemplo_sync()
