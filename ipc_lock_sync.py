from multiprocessing import Process, Lock
import time

def tarea(nombre, lock):
    lock.acquire()
    try:
        print(f"{nombre} está usando el recurso")
        time.sleep(2)
    finally:
        print(f"{nombre} liberó el recurso")
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    p1 = Process(target=tarea, args=("Proceso 1", lock))
    p2 = Process(target=tarea, args=("Proceso 2", lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
