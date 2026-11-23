from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
MODULES = {
    "1": ("Сортировка чисел", "Sorting"),
    "2": ("Суммы диагоналей", "Diagonals"),
    "3": ("Определитель матрицы", "Determinant"),
    "4": ("Минимальный элемент матрицы", "Minimum"),
}


def main():
    while True:
        print("\nЛабораторная работа №2 — вариант 1")
        for key, (title, _) in MODULES.items():
            print(f"{key}. {title}")
        print("0. Выход")

        choice = input("Выберите программу: ").strip()
        if choice == "0":
            return
        if choice not in MODULES:
            print("Нет такого пункта.")
            continue

        title, folder = MODULES[choice]
        script = ROOT / folder / "main.py"
        if not script.is_file():
            print("Модуль не загружен. Выполните:")
            print("git submodule update --init --recursive")
            continue

        print(f"\nЗапуск: {title}")
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=script.parent,
        )
        if result.returncode != 0:
            print("Программа завершилась с ошибкой.")
        input("\nНажмите Enter для возврата в меню.")


if __name__ == "__main__":
    main()
