door_is_open = True        #Переменная, определяющая, открыта или закрыта дверь
door_is_unlocked = True    #Перемнная, определяющая, заблокирована или разблокирована дверь
code_of_door = 1234        #Код от двери
action = 0                 #Выбранное действие

while door_is_unlocked == True:
    print("Дверь открыта. В этой комнате хранятся секретные данные! Нужно срочно её закрыть! Выберите действие: ")
    print("1. Закрыть дверь")
    print("2. Уйти")
    action = int(input())
    if action==1:
        door_is_open = False
        while door_is_unlocked == True:
            print("Дверь закрыта! Давайте заблокируем дверь. Выберите действие:")
            print("1. Заблокировать дверь")
            print("2. Уйти")
            action = int(input())
            if action == 1:
                while door_is_unlocked == True:
                    print("Введите код от двери. Подсказка: у вас в руках листочек с кодом - 1234.")
                    code_of_door = int(input())
                    if code_of_door == 1234:
                        print("Вы успешно заблокировали дверь! Теперь можно уходить.")
                        door_is_unlocked = False
                    else:
                        print("Вы ввели неверный код. Попробуйте ещё раз!")
            elif action==2:
                print("Ну вот, вы не решились заблокировать дверь. Придётся начинать сначала!")
    elif action == 2:
        print("Ну вот, вы не решились закрыть дверь. Придётся начинать сначала!")

        
