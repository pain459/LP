import os
import psycopg2 as pg
import re


def get_db_connection(options):
    postgres_password = re.split(r'\s+',os.popen("sudo -u <user> vault read <path>").read())[7]
    conn = pg.connect(host='<server_name>', dbname='<dbname>', user='<user>', password=postgres_password)
    cur  = conn.cursor()
    return cur.execute("SELECT * FROM pays")
    conn.close()


checker = get_db_connection('<dbname>')

print(checker)
