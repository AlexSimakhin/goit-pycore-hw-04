def total_salary(path):
  try:
    total_salary = 0  # Загальна сума заробітної плати
    num_developers = 0  # Кількість розробників
    
    # Відкриття файлу для читання з заданого шляху
    with open(path, "r", encoding="utf-8") as file:
      for line in file:
        # Розбиття рядка на дві частини: ім'я розробника та зарплата
        parts = line.strip().split(",")
        
        if len(parts) == 2:
          try:
            total_salary += int(parts[1])  # Додавання зарплати до загальної суми
            num_developers += 1  # Збільшення кількості розробників
          except ValueError:
            print(f"Error: Invalid salary format '{line.strip()}'")
            
        else:
          print(f"Error: Invalid data format '{line.strip()}'")
          
    if num_developers > 0:
      # Обчислення середньої зарплати
      average_salary = total_salary / num_developers
      return total_salary, average_salary
    
    else:
      print("Error: No developer salary data in the file.")
      return 0, 0
    
  except FileNotFoundError:
    # Повідомлення про те, що файл не знайдено
    print("Error: File not found.")
    return 0, 0

total, average = total_salary("task1/salary_file.txt")
print(f"Total salary sum: {int(total)}, Average salary: {int(average)}")