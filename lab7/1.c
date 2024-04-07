#include <windows.h>
#include <stdio.h>

// Функция-обработчик сообщений окна
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_KEYDOWN: {
            // Получаем код нажатой клавиши
            int key = wParam;
            // Выводим код клавиши на экран
            printf("Key pressed: %d\n", key);
            break;
        }
        case WM_DESTROY:
            // Закрываем приложение при закрытии окна
            PostQuitMessage(0);
            break;
        default:
            // Передаем все остальные сообщения стандартному обработчику
            return DefWindowProc(hwnd, uMsg, wParam, lParam);
    }
    return 0;
}

int main() {
    // Задаем параметры окна
    WNDCLASS wc = {0};
    wc.lpfnWndProc = WindowProc; // Функция-обработчик сообщений окна
    wc.hInstance = GetModuleHandle(NULL);
    wc.lpszClassName = L"KeyboardTracker";

    // Регистрируем класс окна
    RegisterClass(&wc);

    // Создаем окно
    HWND hwnd = CreateWindowEx(
        0,                      // Нет дополнительных стилей
        L"KeyboardTracker",     // Имя класса окна
        L"Keyboard Tracker",    // Заголовок окна
        0,                      // Стандартный стиль окна
        0, 0, 0, 0,             // Размер и положение окна (будет автоматически определено)
        NULL, NULL,             // Нет родительского именованного окна
        GetModuleHandle(NULL),  // Дескриптор экземпляра приложения
        NULL);

    // Отображаем окно
    ShowWindow(hwnd, SW_SHOW);

    // Запускаем цикл обработки сообщений окна
    MSG msg = {0};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}