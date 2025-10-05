import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def hello_msg():
    messagebox.showinfo(title="Info Message", 
                        message="You pressed the button!")

# Создаём главное окно приложения (root window)
root = tk.Tk()

# Устанавливаем заголовок окна
root.title("First Tkinter Example")

# Устанавливаем размеры окна: 
# Ширина 300 x Высота 100 + X_Коорд 600 + Y_Коорд 300
root.geometry("300x100+600+300")

# Добавляем нативный стиль для окна
style = ttk.Style(root)
style.theme_use('winnative') 

# Создаём текстовую метку (Label)
label = tk.Label(root, text="Hello, Tkinter!")

# Размещаем метку в окне с помощью менеджера grid (нумерация от нуля)
# row=0, column=0 означает: первая строка, первый столбец
label.grid(row=0, column=0, padx=20, pady=20)

# Создаём кнопку (Button)
button = tk.Button(root, text="Press Me",command=hello_msg)

# Размещаем кнопку в той же строке что и Label,
# но уже во второй колонке row=0, column=1
button.grid(row=0, column=1, padx=20, pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()
