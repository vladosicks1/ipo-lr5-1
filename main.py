string = str(input("Введите строку: ")) # ввод строки
print("Длина строки:",len(string)) # вывод длины строки

glasn = 0 
soglasn = 0 # создание переменных для подсчета гласных и согласных букв

string = string.lower() # приведение строки к нижнему регистру 

gl = ["а","у","о","и","э","е","ё","я","ю"] # список с гласными буквами

for i in string: # проверка букв
    if i in gl:
        glasn+=1
    elif i ==" " or i=="!" or i=="?" or i==".":
        continue
    else:
        soglasn+=1
        
print("Количество гласных: ",glasn)
print("Количество согласных: ",soglasn)