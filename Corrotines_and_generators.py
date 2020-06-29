
import time

def retorna():
    time.sleep(60)
    return "string retornada"


def some_generator():
    yield 1
    yield 2
    yield 3
    yield 4

    # return resultado


class Awaitable:
    def __await__(self):
        return some_generator()

async def some_corrotine():
    await Awaitable()
        

generator = some_generator()

next(generator)

corrotine = some_corrotine()

try:
    corrotine.send(None)
except StopIteration as e:
    print(e.value)