
def chek_year():
    year = int(input('Введите год '))
    year = year % 4
    if year == 0:
        print("Високосный ")
    else:
        print("Обычный год")


def lucky_ticket(ticket):
    num1 = ticket % 10
    num2 = ticket % 100 // 10
    num3 = ticket % 1000 // 100
    num4 = ticket % 10000 // 1000
    num5 = ticket % 100000 // 10000
    num6 = ticket % 1000000 // 100000
    if num1 + num2 + num3 == num4 + num5 + num6:
        return True
    else:
        return  False