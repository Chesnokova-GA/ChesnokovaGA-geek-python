"Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет"
"и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. "
"Важно, чтобы для каждого предмета не обязательно были все типы занятий. "
"Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран."
"Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб)."
"Физика: 30(л) — 10(лаб)"
"Физкультура: — 30(пр) —"
"Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"

subjects = {}
name = ""
result = {}

with open("Task05_06_Data.txt", "rt", encoding='utf8') as Lessons_file:
    content = Lessons_file.readlines()
    sum_line = 0
    for line in content:
        subject = line.split()
        name1 = subject[0].rstrip(":")
        if subject[1].find(":") != -1:
            name2 = subject[1].rstrip(":")
            name = ' '.join([name1, name2])
            subjects[name] = subject[2:]
        else:
            name = name1
            subjects[name] = subject[1:]
            #print(name1)
        #print(subject)

       # subjects[name] = sum([int(sj.rstrip('(')) for sj in subject])

    for name, value in subjects.items():
        result[name] = sum([int(sj[:sj.index("(")]) for sj in value if sj != "-"])
    #print(subjects)
    print(result)




