import os
#1
file_1_path = os.path.abspath('data_path_1/test_file_1.txt')
print("Нормализованный абсолютный путь к test_file_1.txt:", file_1_path)
#2
print("\nСодержимое папки проекта:")
for root, dirs, files in os.walk('.'):
    print(f"Текущая директория: {root}")
    for dir_name in dirs:
        print(f"  Подкаталог: {dir_name}")
    for file_name in files:
        print(f"  Файл: {file_name}")
#3
file_3_path = os.path.join(os.path.abspath('data_path_2'), 'test_file_3.txt')
print("\nНормализованный абсолютный путь к test_file_3.txt:", file_3_path)
#4
new_folder_path = os.path.join('data_path_2', 'new_folder')
os.makedirs(new_folder_path, exist_ok=True)
print(f"\nСоздана папка: {new_folder_path}")

os.rmdir(new_folder_path)
print(f"Удалена папка: {new_folder_path}")