def add_contact(contact_data: list, contacts: dict) -> str:
  try:
    # Перевірка, чи передано рівно 2 аргументи (ім'я та телефон)
    if len(contact_data) != 2:
      raise ValueError("Exactly 2 arguments (name and phone) are required.")
    
    name, phone = contact_data
    
    # Додавання нового контакту у словник
    contacts[name] = phone
    return "Contact added."
  
  except ValueError as ve:
    return str(ve)
  
  except Exception as e:
    return f"Error occurred while adding contact: {type(e).__name__}, {e}"


def change_contact(contact_data: list, contacts: dict) -> str:
  try:
    # Перевірка, чи передано рівно 2 аргументи (ім'я та телефон)
    if len(contact_data) != 2:
      raise ValueError("Exactly 2 arguments (name and phone) are required.")
    
    name, phone = contact_data
    
    # Перевірка, чи існує контакт
    if name not in contacts:
      return "Contact does not exist"
    
    # Оновлення контактної інформації
    contacts[name] = phone
    
    return "Contact updated."
  
  except ValueError as ve:
    return str(ve)
  
  except Exception as e:
    return f"Error occurred while changing contact: {type(e).__name__}, {e}"


def get_contact(contact_data: list, contacts: dict) -> str:
  try:
    # Перевірка, чи передано рівно 1 аргумент (ім'я)
    if len(contact_data) != 1:
      raise ValueError("Exactly 1 argument (name) is required.")
    
    name = contact_data[0]
    
    # Перевірка, чи існує контакт
    if name not in contacts:
      return "Contact does not exist"
    
    # Повернення телефонного номера
    return contacts[name]
  
  except ValueError as ve:
    return str(ve)
  
  except Exception as e:
    return f"Error occurred while getting contact: {type(e).__name__}, {e}"


def get_all_contacts(contacts: dict) -> str:
  # Перевірка, чи є контакти в словнику
  if not contacts:
    return "Contacts are empty"
  
  # Формування списку контактів для виведення
  output = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
  return "Contacts:\n" + output
  

def remove_contact(contact_data: list, contacts: dict) -> str:
  try:
    # Перевірка, чи передано рівно 1 аргумент (ім'я)
    if len(contact_data) != 1:
      raise ValueError("Exactly 1 argument (name) is required.")
    
    name = contact_data[0]
    
    # Перевірка, чи існує контакт
    if name not in contacts:
      return "Contact does not exist"
    
    # Видалення контакту
    del contacts[name]
    return "Contact removed."
  
  except ValueError as ve:
    return str(ve)
  
  except Exception as e:
    return f"Error occurred while removing contact: {type(e).__name__}, {e}"