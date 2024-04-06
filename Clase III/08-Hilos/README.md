# Procesos síncronos y asíncronos

Python es un lenguaje síncrono que admite procesos asíncronos, esto quiere decir que dos o más tareas pueden ejecutarse al mismo tiempo pero no de manera pararela, sino más bien de manera concurrente.

# Procesos síncronos

Son procesos que se ejecutan uno por uno, parecido a una estructura de datos de cola, donde las tareas se completan una por una.

# Procesos asíncronos

Son procesos que se ejecutan de forma paralela o concurrente, pero ¿Qué significa esto? 🤔

- Paralelo: tareas que se ejecutan y terminan al mismo tiempo
- Concurrente: tareas que se ejecutan y terminan en tiempos diferentes pero se ejecutan de manera asíncrona

# Procesos asíncronos: Threading (hilos)

Python posee una librería nativa llamada threading que admite la ejecución de tareas asíncronas, son tareas que se ejecutan en el sub-proceso principal de Python, funciona para tareas pequeñas y que no requieren mucho cálculo de computo.

```$
import threading
import time
import os


def get_users():
    time.sleep(2)

    print(['ronald', 'max'])


def get_products():
    time.sleep(1)

    print(['coca-cola', 'pepsi'])


# async tasks
task1 = threading.Thread(target=get_users, args=())
task2 = threading.Thread(target=get_products, args=())

task1.start()

# sync
# task1.join()

task2.start()

# sync
# task2.join()


def complex_calculation(x, y):
    time.sleep(3)

    print(threading.current_thread().name)

    global thread_result

    thread_result = x + y


task3 = threading.Thread(target=complex_calculation,
                         args=(10, 20,), name='complex_calculation')

task3.start()
task3.join()

# None
print(thread_result)

# pid
print(os.getpid())
```
