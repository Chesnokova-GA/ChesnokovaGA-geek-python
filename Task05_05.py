"Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами."
"Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."

from random import randrange

rand_numbers = [randrange(1,100) for n in range(10)]
with open("Task05_05_Date.txt", "w") as file_05_wr:
    #for number in rand_numbers:
        #new_numbers = str(number).join(" ")
        #new_numbers = " ".join(str(number))
        new_numbers = " ".join(map(str, rand_numbers))
       #print(new_numbers)
        file_05_wr.write(new_numbers)
    #file_05.write(map(str(rand_numbers).join(str(" "))))
    #file_05.write(" ")
#print(rand_numbers)

with open("Task05_05_Date.txt", "r") as file_05_r:
    all_numbers = file_05_r.read().split()
    sum_numbers = sum(float(n) for n in all_numbers)

print(sum_numbers)
