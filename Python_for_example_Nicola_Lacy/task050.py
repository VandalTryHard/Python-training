bottles = 10

while bottles > 0:
    print(f"There are {bottles} green bottles hanging on the wall, {bottles} green bottles \
hanging on the wall, and if 1 green bottle should accidentally fall")
    user_bottles = int(input("How many green bottles will be hanging on the wall? "))
    bottles = bottles - 1
    if user_bottles == bottles:
        print(f"There will be {bottles} green bottles hanging on the wall.")
    
    else:
        while user_bottles != bottles:
            user_bottles = int(input("No, try again: "))
    #elif user_bottles != bottles:
        #user_bottles = int(input("No, try again: "))

print("There are no more green bottles hanging on the wall")