import sqlite3

file_db = 'mebel.db'


def create_db(file_db, sql):
    with sqlite3.connect(file_db) as db:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()


def create_table(db_name, table_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute('''
        CREATE


if __name__ == "__main__":
    sql = '''
    CREATE TABLE IF NOT EXISTS persons
    (personID integer,
    f_name text,
    l_name text,
    phone text,
    PRIMARY KEY(personID)
    )
    '''
    create_db(file_db, sql)
