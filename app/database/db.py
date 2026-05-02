import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="db",          # docker service name
        database="mydb",
        user="postgres",
        password="postgres"
    )
    return conn
