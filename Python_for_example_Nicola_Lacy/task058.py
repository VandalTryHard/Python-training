import random
again = 0
correct = 0
while again < 5:
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    result = num1 + num2
    answer = int(input(f"{num1} + {num2} =  "))
    again = again + 1
    out_of = 5
    if answer == result:
        print("Yep")
        correct = correct + 1
        print(f"{correct} out of {out_of}")
    elif answer != result:
        print("Nop")
        print(f"{correct} out of {again}")
print(f"Total {correct} out of {again}")
