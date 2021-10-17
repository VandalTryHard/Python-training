"""Предложите пользователю ввести пароль, а затем
предложите ввести его повторно. Если два пароля со-
впадут, выведите сообщение «Thank you». Если буквы
введены правильно, но различаются регистром, вы-
ведите сообщение «They must be in the same case»;
в противном случае выводится сообщение «Incorrect»."""

user_password = input("Enter password: ")
examination = True
password_verification = input("Repeat password: ")
while examination == True:
    if password_verification.lower() != user_password.lower():
        password_verification = input("Incorrect! Try again: ")
    elif password_verification != user_password:
        print("They must be in the same case")
        password_verification = input("Incorrect! Try again: ")
        continue
    elif password_verification == user_password:
        examination = False
print("Successfully")

