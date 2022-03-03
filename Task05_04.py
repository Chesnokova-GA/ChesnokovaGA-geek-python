"Создать (не программно) текстовый файл со следующим содержимым:"
"One — 1"
"Two — 2"
"Three — 3"
"Four — 4"
"Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные."
"При этом английские числительные должны заменяться на русские. "
"Новый блок строк должен записываться в новый текстовый файл."

russian_words = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"}

new_list = []

with open("Task05_04_data", "rt") as original_file:
   m_content = original_file.readlines()
   for m_line in m_content:
      my_key, value = m_line.split(' - ')
      new_list.append(f"{russian_words[my_key]} - {value}")
      #print(original_file.readlines())
      #print(f"{my_key} , {value}")
      #print(new_list)

with open("Task05_04_new_data.txt", "w") as new_file:
    new_file.writelines(new_list)
