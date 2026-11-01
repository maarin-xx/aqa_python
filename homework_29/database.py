import psycopg2

# Параметри підключення
# База даних повинна існувати на зазначеному хості, та юзер повинен мати право на читання цього запису
dbname = 'homework29'
user = 'test_user'
password = 'test_password'
host = 'db'
port = '5432'

def get_connection():
    # Спроба підключитись до бази даних
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return connection

    except (Exception, psycopg2.Error):
        raise
