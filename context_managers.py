import pymysql

class FileManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file and not self.file.closed:
            self.file.close()


class DatabaseConnect:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = pymysql.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection and self.connection.open:
            self.connection.close()


class Person:
    @staticmethod
    def get_all_persons(db_info):
        with DatabaseConnect(**db_info) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM person;")
                return cursor.fetchall()

    @staticmethod
    def get_one_person(db_info, id):
        with DatabaseConnect(**db_info) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM person WHERE id = %s;", (id,))
                return cursor.fetchone()


db_info = {
    "host": "localhost",
    "database": "n56_database",
    "user": "root",
    "password": "Jasur1010",
    "port": 3306
}

print(Person.get_all_persons(db_info))
print(Person.get_one_person(db_info, id = 1))



