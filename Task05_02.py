"Создать текстовый файл (не программно), сохранить в нем несколько строк, "
"выполнить подсчет количества строк, количества слов в каждой строке."

with open('Task05_02_Data', 'rt') as f_obj:
    content = f_obj.readlines()
    #lines = [line.strip() for line in content]
    #lines_count = lines.count()
    lines_count = len(content)
    words = [line.split() for line in content]
    #word_count = len(words)
    words_count = sum([len(word) for word in words])

print(f"Количество строк: {lines_count}, Всего количество слов: {words_count}")
count = 0
for word in words:
    words_count2 = len(word)
    count += 1
    print(f"Количество слов в строке {count}: {words_count2}")



