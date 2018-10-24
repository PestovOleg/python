my=input("Загадайте число ")
while True:
    your=input("Отгадай число ")
    if your==my:
        print("Вы отгадали число! ",my)
        break
    elif your<my:
        print("Вы не отгадали число, нужно больше")
    elif your>my:
        print("Вы не отгадали число, нужно меньше")