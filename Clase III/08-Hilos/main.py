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

print('----------------------------------------------------------------')
