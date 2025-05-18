from multiprocessing import Process, Semaphore
import time

def tarea(nombre, semaforo):
    print(f"{nombre} quiere acceder")
    semaforo.acquire()  # Entra si hay lugar (permiso disponible)
    try:
        print(f"{nombre} accedió al recurso")
        time.sleep(2)  # Simula trabajo
    finally:
        print(f"{nombre} liberó el recurso")
        semaforo.release()  # Devuelve el permiso

if __name__ == '__main__':
    semaforo = Semaphore(2)  # Permite hasta 2 procesos a la vez
    procesos = []

    for i in range(5):
        p = Process(target=tarea, args=(f"Proceso {i+1}", semaforo))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()
