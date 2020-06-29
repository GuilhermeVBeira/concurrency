from time import sleep
import time


def cozinha_macarrao(i):
    print(f"Preparando macarrão {i}")
    sleep(15)
    print(f"Macarrao pronto {i}")


def pegar_macarrao(i):
    print(f"Pegando macarrão {1} para cozinha")
    sleep(3)


def preparar_macarrao(i):
    pegar_macarrao(i)
    cozinha_macarrao(i)


t0 = time.perf_counter()
for i in range(2):
    preparar_macarrao(i)
dt = time.perf_counter(i) - t0
print(f"Finished in : {dt:0.3}s")