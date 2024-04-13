import tkinter as tk
import winreg


def create_registry_key():
    key_path = key_entry.get()
    value_name = value_entry.get()
    value_data = data_entry.get()
    
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
        _, _ = winreg.QueryValueEx(key, value_name)
        result_text.set(f"Ошибка: Значение с именем '{value_name}' уже существует в указанном ключе.")
    except FileNotFoundError:
        try:
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
            result_text.set("Значение успешно создано.")
        except Exception as e:
            result_text.set(f"Ошибка: {str(e)}")
    except Exception as e:
        result_text.set(f"Ошибка: {str(e)}")


def read_registry_values():
    key_path = key_entry.get()
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path)
        values = []
        i = 0
        while True:
            try:
                value_name, value_data, _ = winreg.EnumValue(key, i)
                values.append(f"Значение: {value_name} - Данные: {value_data}")
                i += 1
            except OSError:
                break
        result_text.set("\n".join(values))
    except Exception as e:
        result_text.set(f"Ошибка: {str(e)}")


def delete_registry_value():
    key_path = key_entry.get()
    value_name = value_entry.get()
    
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, value_name)
        result_text.set("Значение успешно удалено.")
    except Exception as e:
        result_text.set(f"Ошибка: {str(e)}")


# Создание графического интерфейса
root = tk.Tk()
root.title("lab9")
root.resizable(False, False) 

# Поля ввода
key_label = tk.Label(root, text="Путь к ключу:")
key_label.grid(row=0, column=0)
key_entry = tk.Entry(root)
key_entry.grid(row=0, column=1)

value_label = tk.Label(root, text="Имя значения:")
value_label.grid(row=1, column=0)
value_entry = tk.Entry(root)
value_entry.grid(row=1, column=1)

data_label = tk.Label(root, text="Данные значения:")
data_label.grid(row=2, column=0)
data_entry = tk.Entry(root)
data_entry.grid(row=2, column=1)

# Кнопки
create_button = tk.Button(root, text="Создать значение", command=create_registry_key)
create_button.grid(row=3, column=0)

read_button = tk.Button(root, text="Прочитать значение", command=read_registry_values)
read_button.grid(row=3, column=1)

delete_button = tk.Button(root, text="Удалить значение", command=delete_registry_value)
delete_button.grid(row=3, column=2)

# Поле вывода
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=4, column=0, columnspan=3)

root.mainloop()