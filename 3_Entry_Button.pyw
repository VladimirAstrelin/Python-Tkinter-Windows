import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Функция-обработчик для кнопки
def change_text():
    # Получаем текст, который пользователь ввёл в Entry
    user_text = entry.get()
    # Если строка пустая — показываем предупреждение
    if not user_text.strip():
        messagebox.showwarning(title="Warning", message="Please enter some text!")
        return
    # Меняем текст метки на введённое значение
    label.config(text=user_text)
    # Дополнительно выводим всплывающее окно
    messagebox.showinfo(title="Info Message", 
                        message="Label Text has been changed!")

# Создаём главное окно приложения (root window)
root = tk.Tk()

# Устанавливаем заголовок окна
root.title("Third Tkinter Example")

# Устанавливаем размеры окна и его положение:
# 300x100 — размеры; +600+300 — позиция относительно верхнего левого угла экрана
root.geometry("300x100+600+300")

# Добавляем нативный стиль для окна
style = ttk.Style(root)
style.theme_use('winnative')

# Создаём текстовую метку (Label)
label = tk.Label(root, text="Hello, Tkinter!")

# Размещаем метку в первой строке, первая колонка
label.grid(row=0, column=0, padx=10, pady=10)

# Создаём кнопку (Button), которая вызывает функцию change_text
button = tk.Button(root, text="Change Text", command=change_text)

# Размещаем кнопку в той же строке, но во второй колонке
button.grid(row=0, column=1, padx=10, pady=10)

# Создаём поле ввода текста (Entry)
entry = tk.Entry(root, width=25)

# Размещаем Entry во второй строке, первая колонка (растянем на 2 колонки через columnspan=2)
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Запускаем главный цикл обработки событий
root.mainloop()
