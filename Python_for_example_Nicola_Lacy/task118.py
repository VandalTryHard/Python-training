"""Определите подпрограмму, которая предлагает пользо-
вателю ввести число и сохраняет его в переменной num.
Определите другую подпрограмму, которая использует
значение num и проводит отсчет от 1 до этого числа."""

def ask_num():
    num = int(input("Number: "))
    return num

def use_num(num):
    for i in range(0, num):
        print(i + 1)

def main():
    num = ask_num()
    use_num(num)

main()


