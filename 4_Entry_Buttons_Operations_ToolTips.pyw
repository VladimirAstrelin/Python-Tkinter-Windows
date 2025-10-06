import tkinter as tk                                   # Импортируем основной модуль tkinter под коротким именем tk
from tkinter import ttk                                # Импортируем ttk — набор современных виджетов/стилей

# --- Создаём главное окно приложения ---
root = tk.Tk()                                         # Создаём корневое (главное) окно приложения
root.title("Entry Field Operations with Tooltips")     # Устанавливаем заголовок окна
style = ttk.Style(root)                                # Создаём объект стиля ttk, привязанный к root
style.theme_use('winnative')                           # Применяем нативную тему (на Windows даст нативный вид)
root.geometry("420x180+600+300")                       # Устанавливаем размер окна и позицию на экране

# --- Настройка поведения колонок для корректного растяжения виджетов ---
root.columnconfigure(0, weight=1)                      # Позволяем первой колонке растягиваться при изменении ширины окна
root.columnconfigure(1, weight=1)                      # То же для второй колонки

# --- Переменная для привязки к Entry (StringVar) ---
entry_text = tk.StringVar()                            # Создаём StringVar для хранения текста поля Entry
entry_text.set("Initial Text")                           # Устанавливаем начальное значение, чтобы кнопки были активны при старте

# --- Создаём Entry (поле ввода) ---
entry = ttk.Entry(root, textvariable=entry_text, width=40)  # Создаём виджет Entry, связанный с entry_text
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")  # Размещаем Entry в первой строке, растягиваем по ширине

# --- Словарь для хранения всплывающих подсказок (чтобы управлять окном подсказки) ---
_tooltips = {}                                        # Пустой словарь: ключ = виджет, значение = окно подсказки (Toplevel)

def _show_tooltip(widget, text):
    """Показать подсказку рядом с виджетом. (вспомогательная, приватная)"""
    # Удаляем старую подсказку для этого виджета, если она есть (предотвращаем наложение)
    _hide_tooltip(widget)                              # Если уже есть — удаляем
    # Создаём плавающее окно без рамок (overrideredirect=True) — это будет наша подсказка
    tip = tk.Toplevel(root)                            # Создаём Toplevel, дочерний по отношению к root
    tip.wm_overrideredirect(True)                      # Убираем титул и рамку окна — выглядит как tooltip
    # Получаем координаты виджета в глобальных координатах экрана
    x = widget.winfo_rootx() + 20                      # Смещаем подсказку немного вправо от виджета
    y = widget.winfo_rooty() + widget.winfo_height() + 1  # Размещаем подсказку под виджетом
    tip.wm_geometry(f"+{x}+{y}")                       # Устанавливаем позицию подсказки
    # Создаём метку внутри Toplevel с лаконичным оформлением — она и будет текстом подсказки
    label = tk.Label(tip, text=text, justify="left", relief="solid", borderwidth=1,
                     background="#ffffe0", padx=4, pady=2)  # Стандартный "tooltip" стиль (светло-жёлтый фон)
    label.pack()                                       # Упаковываем метку внутрь окна подсказки
    _tooltips[widget] = tip                            # Сохраняем ссылку на окно подсказки в словаре

def _hide_tooltip(widget):
    """Скрыть подсказку для виджета (если она показана)."""
    tip = _tooltips.pop(widget, None)                  # Получаем и удаляем запись из словаря
    if tip:
        try:
            tip.destroy()                              # Уничтожаем окно подсказки (если существует)
        except Exception:
            pass                                       # На случай, если окно уже уничтожено

def create_tooltip(widget, text):
    """Привязать подсказку к виджету: показывать при наведении, скрывать при уходе курсора."""
    # При наведении курсора показываем подсказку
    widget.bind("<Enter>", lambda e: _show_tooltip(widget, text))
    # При уходе курсора (или при щелчке) скрываем подсказку
    widget.bind("<Leave>", lambda e: _hide_tooltip(widget))
    widget.bind("<ButtonPress>", lambda e: _hide_tooltip(widget))  # Скрывать при нажатии — удобно для UX

# --- Функции-обработчики операций над Entry ---
def select_range():
    """Выделить диапазон символов в Entry (индексы 2..7)."""
    entry.focus_set()                                   # Устанавливаем фокус ввода в Entry (пользователь видит курсор)
    entry.selection_clear()                             # Снимаем старое выделение (на всякий случай)
    # Безопасно вычисляем окончание (в случае короткой строки избегаем ошибки)
    try:
        length = int(entry.index(tk.END))               # Получаем длину текста (индекс после последнего символа)
    except Exception:
        length = len(entry_text.get())                  # Запасной вариант вычисления длины
    start = 2                                           # Начальный индекс выделения
    end = min(8, length)                                # Конечный индекс — не включается, ограничиваем длиной
    if start < end:
        entry.select_range(start, end)                  # Выделяем текст в заданном диапазоне

def select_all():
    """Выделить весь текст в Entry."""
    entry.focus_set()                                   # Устанавливаем фокус ввода
    entry.selection_range(0, tk.END)                    # Выделяем от 0 до END (весь текст)

def delete_range():
    """Удалить символы в диапазоне 2..7 (если они есть)."""
    entry.focus_set()                                   # Устанавливаем фокус ввода
    try:
        length = int(entry.index(tk.END))               # Получаем текущую длину текста
    except Exception:
        length = len(entry_text.get())                  # Запасной вариант
    if length > 2:
        end_idx = min(8, length)                        # Определяем безопасный конечный индекс
        entry.delete(2, end_idx)                        # Удаляем символы от 2 до end_idx (не включая end_idx)

def clear_entry():
    """Очистить всё содержимое Entry."""
    entry.delete(0, tk.END)                             # Удаляем все символы: от 0 до END

def insert_text():
    """Вставить текст в позицию 5 (или в конец, если строка короче)."""
    entry.focus_set()                                   # Устанавливаем фокус ввода
    pos = 5                                             # Желаемая позиция для вставки
    try:
        length = int(entry.index(tk.END))               # Получаем длину текста
    except Exception:
        length = len(entry_text.get())                  # Запасной вариант
    if pos > length:
        pos = length                                    # Если позиция за пределами строки — вставляем в конец
    entry.insert(pos, "__Inserted_Text__")              # Вставляем текст по индексу pos

# --- Создаём кнопки и помещаем их в сетку (grid) ---
btn1 = ttk.Button(root, text="Select Range (2-8)", command=select_range)  # Кнопка для выделения диапазона
btn1.grid(row=1, column=0, padx=10, pady=5, sticky="ew")                  # Размещаем в строке 1, колонка 0, растягиваем по ширине

btn2 = ttk.Button(root, text="Select All", command=select_all)            # Кнопка для выделения всего текста
btn2.grid(row=1, column=1, padx=10, pady=5, sticky="ew")                  # Размещаем в строке 1, колонка 1

btn3 = ttk.Button(root, text="Delete Range (2-8)", command=delete_range)  # Кнопка для удаления диапазона
btn3.grid(row=2, column=0, padx=10, pady=5, sticky="ew")                  # Размещаем в строке 2, колонка 0

btn4 = ttk.Button(root, text="Clear Entry", command=clear_entry)          # Кнопка для очистки поля
btn4.grid(row=2, column=1, padx=10, pady=5, sticky="ew")                  # Размещаем в строке 2, колонка 1

btn5 = ttk.Button(root, text="Insert Text at Position 5", command=insert_text)  # Кнопка для вставки текста на позицию 5
btn5.grid(row=3, column=0, columnspan=2, padx=10, pady=8, sticky="ew")    # Размещаем в строке 3, занимает обе колонки

# --- Привязываем подсказки к кнопкам (tooltips) ---
create_tooltip(btn1, "Select characters from index 2 to 7 (if present).")  # Подсказка для btn1
create_tooltip(btn2, "Select all text (Ctrl+A works too).")                # Подсказка для btn2
create_tooltip(btn3, "Delete characters from index 2 to 7 (if present).")  # Подсказка для btn3
create_tooltip(btn4, "Clear the entry field.")                             # Подсказка для btn4
create_tooltip(btn5, "Insert text at position 5 (or end if too short).")   # Подсказка для btn5

# --- Функция обновления состояния кнопок (включать/отключать) в зависимости от содержимого Entry ---
def update_buttons_state(*args):
    """Включать/отключать кнопки в зависимости от того, пусто поле или нет."""
    text = entry_text.get()                            # Получаем текущее содержимое поля из StringVar
    if text.strip() == "":                             # Если после удаления пробелов строка пустая
        # Отключаем кнопки — делаем их неактивными
        btn1.state(["disabled"])                       # Отключаем btn1
        btn2.state(["disabled"])                       # Отключаем btn2
        btn3.state(["disabled"])                       # Отключаем btn3
        btn4.state(["disabled"])                       # Отключаем btn4
        btn5.state(["disabled"])                       # Отключаем btn5
    else:
        # Включаем кнопки — делаем их активными
        btn1.state(["!disabled"])                      # Включаем btn1
        btn2.state(["!disabled"])                      # Включаем btn2
        btn3.state(["!disabled"])                      # Включаем btn3
        btn4.state(["!disabled"])                      # Включаем btn4
        btn5.state(["!disabled"])                      # Включаем btn5

# --- Привязываем отслеживание изменений в StringVar — чтобы автообновление состояния кнопок работало сразу ---
# Для современных tkinter используем trace_add; для совместимости можно добавить trace (старый вариант).
try:
    entry_text.trace_add("write", update_buttons_state)  # При любом изменении entry_text вызываем update_buttons_state
except AttributeError:
    entry_text.trace("w", update_buttons_state)          # Запасной вариант для старых версий tkinter

# --- Инициално вызовем update_buttons_state, чтобы состояние кнопок соответствовало начальному тексту ---
update_buttons_state()                                  # Один вызов при старте: если поле пустое — кнопки будут отключены

# --- Горячие клавиши / привязки ---
root.bind("<Control-a>", lambda e: (select_all(), "break"))  # Ctrl+A — выделить всё; возвращаем "break", чтобы предотвратить стандартный обработчик

# --- Обработчик закрытия окна: перед закрытием прячем все подсказки (чтобы не оставалось плавающих окон) ---
def on_close():
    """Корректное завершение — скрыть все подсказки и закрыть главное окно."""
    # Удаляем все подсказки, если какие-то остались
    for w in list(_tooltips.keys()):
        _hide_tooltip(w)
    root.destroy()                                     # Уничтожаем главное окно и завершаем приложение

root.protocol("WM_DELETE_WINDOW", on_close)           # Подключаем наш on_close к системному событию закрытия окна

# --- Запускаем главный цикл обработки событий приложения ---
root.mainloop()                                       # Запускаем loop — приложение работает пока окно не будет закрыто
