import sqlite3
def create_tables():
    con = sqlite3.connect('users.db')
    cursor = con.cursor()
    cursor.execute('''
        create table if not exists users
        (
            id integer primary key autoincrement,
            fio text not null,
            login text not null,
            password text not null,
            age integer
        )
    ''')


def reguser(fio, login, password, age):
    con = sqlite3.connect('users.db')
    cursor = con.cursor()
    cursor.execute('insert into users (fio, login, password, age) values (?,?,?,?)', (fio, login, password, age))
    con.commit()


def authlogin(login):
    con = sqlite3.connect('users.db')
    cursor = con.cursor()
    cursor.execute('select * from users where login = ?', (login,))
    if cursor.fetchone():
        return True
    return False

def authuser(login ,password):
    con = sqlite3.connect('users.db')
    cursor = con.cursor()
    cursor.execute('select * from users where login = ? and password = ?', (login, password))
    if cursor.fetchone():
        return True
    return False