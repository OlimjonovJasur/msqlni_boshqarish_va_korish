import pymysql

db_info = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'Jasur1010',
    'database' : 'n56_database'
}

class DatabaseConnect:
    def __init__(self, host, port, user, password, database):
        self.connection_params = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'database': database
        }

    def __enter__(self):
        self.connection = pymysql.connect(**self.connection_params)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


class Person:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def save(self):
        with DatabaseConnect(**db_info) as connection:
            with connection.cursor() as cursor:
                create_table_person = '''
                    create table if not exists person(
                        id int auto_increment primary key,
                        full_name varchar(100) not null,
                        age int not null
                    );
                    cursor.execute(create_table_person)
                    connection.commit()
                '''

                insert_into_person = '''
                insert into person
                    (full_name, age)
                values
                    (%s, %s);
                '''
                data = (self.full_name, self.age)

                cursor.execute(insert_into_person, data)
                connection.commit()
                print('shaxs muvaffaqqiyatli saqlandi')

ali = Person('Ali', 20)
ali.save()
vali = Person('Vali', 21)
vali.save()
toxir = Person('Toxir', 19)
toxir.save()


