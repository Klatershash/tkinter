import tkinter
from tkinter.messagebox import showerror, showinfo
import db

def reg():
    fio_1 = fio.get()
    login_1 = login.get()
    password_1 = password.get()
    age_1 = age.get()

    if len(fio_1) == 0 or len(login_1) == 0 or len(password_1) == 0 or len(age_1) == 0:
        showerror('Ошибка', 'пустые значения полей')
    else:
        if age_1.isdigit():
            db.create_tables()
            if db.authlogin(login_1):
                showerror('Error', 'Такой логин уже занят')
            else:
                db.reguser(fio_1, login_1, password_1, age_1)
                showinfo('Успешная регисрация', 'Вы успешно зарегистрированы')
        else:
            showerror('Ошибка', 'Некорректно заданый возраст')
def auth():
    login_auth_1 = login_auth.get()
    password_auth_1 = password_auth.get()
    if db.authuser(login_auth_1, password_auth_1):
        showinfo('Сообщение', 'Вы успешно авторизировались')
    else:
        showerror('Error', 'Логи и/или пароль заданые не верно!')


root = tkinter.Tk()
root.title('Регистрация пользователя')
root.geometry('220x400')

fio_label = tkinter.Label(text='ФИО')
fio_label.grid(row=0, column=0, padx=10, pady=10)

fio = tkinter.Entry(root)
fio.grid(row=0, column=1, padx=10, pady=10)

login_label = tkinter.Label(text='Логин')
login_label.grid(row=1, column=0, padx=10, pady=10)

login = tkinter.Entry(root)
login.grid(row=1, column=1, padx=10, pady=10)

password_label = tkinter.Label(text='Пароль')
password_label.grid(row=2, column=0, padx=10, pady=10)

password = tkinter.Entry(root)
password.grid(row=2, column=1, padx=10, pady=10)

age_label = tkinter.Label(text='Возраст')
age_label.grid(row=3, column=0, padx=10, pady=10)

age = tkinter.Entry(root)
age.grid(row=3, column=1, padx=10, pady=10)

btn_reg = tkinter.Button(text='Регистрация', command=reg)
btn_reg.grid(row=4, column=1)



login_auth_label = tkinter.Label(text='Логин')
login_auth_label.grid(row=7, column=0, padx=10, pady=10)
login_auth = tkinter.Entry(root)
login_auth.grid(row=7, column=1, padx=10, pady=10)

password_auth_label = tkinter.Label(text='Пароль')
password_auth_label.grid(row=8, column=0, padx=10, pady=10)
password_auth = tkinter.Entry(root)
password_auth.grid(row=8, column=1, padx=10, pady=10)

btn_reg = tkinter.Button(text='Авторизация', command=auth)
btn_reg.grid(row=9, column=1)



root.mainloop()