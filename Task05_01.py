#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

while True:
    with open('data.txt', 'a+') as text_file:
        user_date = input("Введите текст >>>")
        if not user_date:
            break
        text_file.write(f"{user_date}\n")