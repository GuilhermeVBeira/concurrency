import psycopg2
import string
import random
import time

SQL_INSERT = (
    """ INSERT INTO role (role_id, role_name) VALUES (%(role_id)s, %(role_name)s);"""
)

t0 = time.perf_counter()

def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(string_length))


conn = psycopg2.connect(
    dbname="async_test", user="async_test", password="async_test", host="127.0.0.1"
)

cur = conn.cursor()
tasks = [({"role_id": i, "role_name": random_string()}) for i in range(600000)]
cur.executemany(SQL_INSERT, tuple(tasks))
conn.commit()
cur.close()
conn.close()
dt = time.perf_counter() - t0
print(f"Finished in : {dt:0.3}s")
