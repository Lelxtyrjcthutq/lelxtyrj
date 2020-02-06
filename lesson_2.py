# 1 Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована
for i in range(1, 6): # range(start? stop? step)
    print(i, 0, sep = '. ')

# 2 Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.

result = 0
for i in range(10):
    ans = int(input('Введите значение: '))
    if ans == 5:
        result += 1
print ("Количество пяторок = ", result)

# 3 Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.

sum = 0
for i in range(1,101):
    sum += i
print(sum)

# 4 Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

result = 1
for i in range(1,11):
    result *= i
print(result)

# 5 Вывести цифры числа на каждой строчке.

integer_number = 2129

while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10


# # 6 Найти сумму цифр числа.
integer_number = 2129
sum = 0
while integer_number > 0:
    ost = integer_number % 10
    integer_number = integer_number // 10
    sum += ost
print("сумма рaвна =", sum)


# 7 Найти произведение цифр числа.

integer_number = 2129
proiz = 1
while integer_number > 0:
    ost = integer_number % 10
    integer_number = integer_number // 10
    proiz *= ost
print("произведение равно =", proiz)


# 8 Дать ответ на вопрос: есть ли среди цифр числа 5?

integer_number = 2134135
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')


# 9 Найти максимальную цифру в числе

a = 2921
max = a % 10
a = a // 10
while a > 0:
   if a % 10 > max:
       max = a % 10
   a = a // 10
print(max)

# 10 Найти количество цифр 5 в числе

n = int(input("Введите число: "))
count = 0
while n > 0:
    if n % 10 == 5:
        count += 1
    n = n // 10
print("Было введено", count, "цифр пять")

