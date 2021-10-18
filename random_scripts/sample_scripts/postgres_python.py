import os
import psycopg2 as pg
import re


def get_db_connection(*options):
    #postgres_password = re.split(r'\s+',os.popen("sudo -u <user> vault read <path>").read())[7]
    conn = pg.connect(host='localhost', dbname='testme', user='postgres', password='<load_password')
    cur  = conn.cursor()
    return cur.execute("SELECT * FROM testme.public.customer")
    conn.close()


checker = get_db_connection()

