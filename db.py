import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="autoinsight_db",
            user="postgres",
            password="postgres",
            port="5432"
        )
        return connection
    
    except Exception as error:
        print("Error:", error)
        return None