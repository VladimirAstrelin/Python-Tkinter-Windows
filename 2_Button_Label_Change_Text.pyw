import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Функция-обработчик для кнопки
def change_text():
    # Меняем текст метки через метод .config()
    label.config(text="CHANGED TEXT!")
    # Дополнительно выводим всплывающее окно
    messagebox.showinfo(title="Info Message", 
                        message="Label Text has been changed!")

# Создаём главное окно приложения (root window)
root = tk.Tk()

# Устанавливаем заголовок окна
root.title("Second Tkinter Example")

# Устанавливаем размеры окна и его положение:
root.geometry("300x100+600+300")

# Добавляем нативный стиль для окна
style = ttk.Style(root)
style.theme_use('winnative')

# Создаём текстовую метку (Label)
label = tk.Label(root, text="Hello, Tkinter!")

# Размещаем метку в первой строке, первый столбец
label.grid(row=0, column=0, padx=20, pady=20)

# Создаём кнопку (Button) с привязкой к функции change_text
button = tk.Button(root, text="Press Me", command=change_text)

# Размещаем кнопку во второй строке, первый столбец
button.grid(row=0, column=1, padx=20, pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()
