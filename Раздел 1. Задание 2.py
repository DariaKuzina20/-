liquid_volume = 0    #Переменная, определяющая объем жидкости в стакане
liquid_volume1 = 0   #Переменная, определяющая объем доливаемой жидкости в стакан
liquid_volume2 = 0   #Переменная, определяющая объем наливаемой жидкости из стакана
glass_volume = 0     #Переменная, определяющая объем стакана
action = 0           #Выбираемое действие


print("Введите объем стакана (мл). Строго больше 0: ")
glass_volume = int(input())
while liquid_volume <= glass_volume:
    print("Выберите дальнейшее дествие:")
    print("1. Долить жидкость в стакан")
    print("2. Налить жидкость из стакана")
    print("3. Определить текущее количество жидкости в стакане")
    print("4. Помыть стакан и поставить на место")
    action = int(input())
    if action == 1:
        print ("Введите объем доливаемой жидкости (мл):")
        liquid_volume1 = int(input())
        liquid_volume = liquid_volume + liquid_volume1
        if liquid_volume > glass_volume:
            liquid_volume = liquid_volume - liquid_volume1
            print("Невозможно долить такое количество жидкости в стакан, так как стакан переполнится.")
        else:
            print("Жидкость успешно долита в стакан!")
    if action == 2:
        print("Введите объем наливаемой из стакана жидкости: ")
        liquid_volume2 = int(input())
        if liquid_volume < liquid_volume2:
            print("Невозможно налить такой объем жидкости из стакана, так как в стакане недостаточно жидкости")
        else:
            liquid_volume = liquid_volume - liquid_volume2
            print("Вы успешно налили жидкость из стакана")
    if action == 3:
         print(liquid_volume)
    if action == 4:
        print("Стакан чистый! Вы закончили работу с водой.")
        break
         
