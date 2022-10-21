import math
alph = "0123456789ABCDEF"

while True:
    try:
        n = input("Введите число в десятичной системе счисления: ")
        n = int(n)
        break
    except:
        try:
            n = float(n)
            break
        except:
            print("Некорректный ввод!")


while True:
    try:
        base = int(input("Выберите, в какую систему счисления(от 2 до 16) вы хотите перевести число: "))
        if base >= 2 and base <= 16 and isinstance(base, int):
            break
        else:
            print("Такая система счисления недопступна!")
    except:
        print("Такой системы счисления нет!")

new_n = ""

if isinstance(n, int):
    while n >= base:
        new_n += alph[n % base]
        n = n//base
    new_n += str(n % base)
    new_n = "".join(reversed(new_n))


if isinstance(n, float):
    two = list(str(n).split('.'))

    a = int(two[0])
    a_s = ""

    while a >= base:
        a_s += alph[a % base]
        a = a // base

    a_s += str(a % base)
    a_s = "".join(reversed(a_s))


    b = float("0." + two[1])
    b_s = ''

    counter = 0
    while b % 1 > 0 and counter < 10:
        counter += 1
        b = b * base
        b_s += alph[int(math.floor(b))]
        b = b % 1

    new_n = a_s + '.' + b_s

print(new_n)


