"""Предложите пользователю ввести слово в верхнем регистре. Если
не все буквы слова будут указаны в верхнем регистре, попросите
ввести слово заново. Повторяйте попытки, пока пользователь не
введет сообщение в верхнем регистре."""

user_word = input("Uppercase word: ")
word = False
while word == False:
    for i in user_word:
        if user_word != user_word.upper():
            user_word = input("Please try again: ")
        elif user_word == user_word.upper():
            print("Correct")
            word = True