import random

while True:
    num = random.randint(-5, 5)
    print("Random integer:", num)

    if num > 0:
        print("Head")
        break
    elif num < 0:
        print("Tail")
        break
    else:  # num == 0
        print("Try again...\n")
