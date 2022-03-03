"Создать текстовый файл (не программно), построчно записать фамилии сотрудников "
"и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,"
"вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников."
"Пример файла:"
"Иванов 23543.12"
"Петров 13749.32"

with open("Task05_03_Data.txt", "rt", encoding='utf8') as my_file:
    content = my_file.readlines()

list = [line.split() for line in content]
subjects = [{"name": el[0], "salary": float(el[1])} for el in list]
#print(list)
#print(subjects)

sum_salary = 0
for elem in subjects:
    #sum_salary += (elem["salary"])
    if elem["salary"] < 20000:
        print(elem["name"])

average_salary = sum([value["salary"] for value in subjects])/len(subjects)
print(f"Средний доход сотрудников: {average_salary}")