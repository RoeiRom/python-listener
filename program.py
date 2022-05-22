import json
import threading
import psycopg2
from psycopg2 import extensions

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="example")
connection.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()

cursor.execute(f"LISTEN new_person")


def handle_new_person():
    print("Waiting for notifications on channel 'new_person'")
    while True:
        connection.poll()
        while connection.notifies:
            notify = connection.notifies.pop(0)
            body = json.loads(notify.payload)
            print(f"new user! {body}")


thread = threading.Thread(target=handle_new_person, daemon=True)

thread.start()

while True:
    pass
