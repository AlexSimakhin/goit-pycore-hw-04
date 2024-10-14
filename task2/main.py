def get_cats_info(path):
  cats_list = []  # Список для зберігання інформації про котів
  
  try:
    # Відкриття файлу для читання з заданого шляху
    with open(path, "r", encoding="utf-8") as file:
      for line in file:
        # Розбиття рядка на три частини: id, ім'я кота та вік
        parts = line.strip().split(",")
        
        if len(parts) == 3:
          # Створення словника з інформацією про кота
          cat_info = {"id": parts[0], "name": parts[1], "age": parts[2]}
          cats_list.append(cat_info)  # Додавання словника до списку
          
        else:
          # Виведення повідомлення про помилку, якщо формат даних неправильний
          print(f"Error: Invalid data format '{line.strip()}'")
          
  except FileNotFoundError:
    print("Error: File not found.")
    
  return cats_list  # Повернення списку з інформацією про котів

cats_info = get_cats_info("task2/cats_file.txt")
print(cats_info)