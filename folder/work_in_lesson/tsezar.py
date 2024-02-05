while True:
    a = int(input('Выберите операцию:\n1. Шифровка\n2. Дешифровка\n3. Выход\nВведите число: '))

    if a == 1:
        alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        offset = int(input('Шаг шифровки: '))
        message = input("Сообщение для шифровки: ").upper()
        result = ''
        lang = input('Выберите язык RU/EU: ')
        if lang == 'RU':
            for i in message:
                if i in alfavit_RU:
                    place = alfavit_RU.find(i)
                    new_place = (place + offset) % len(alfavit_RU)
                    result += alfavit_RU[new_place]
                else:
                    result += i
        else:
            for i in message:
                if i in alfavit_EU:
                    place = alfavit_EU.find(i)
                    new_place = (place + offset) % len(alfavit_EU)
                    result += alfavit_EU[new_place]
                else:
                    result += i
        print(result)

    elif a == 2:
        alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        offset = int(input('Шаг дешифровки: '))
        message = input("Сообщение для дешифровки: ").upper()
        result2 = ''
        lang = input('Выберите язык RU/EU: ')
        if lang == 'RU':
            for i in message:
                if i in alfavit_RU:
                    place = alfavit_RU.find(i)
                    new_place = (place - offset) % len(alfavit_RU)
                    result2 += alfavit_RU[new_place]
                else:
                    result2 += i
        else:
            for i in message:
                if i in alfavit_EU:
                    place = alfavit_EU.find(i)
                    new_place = (place - offset) % len(alfavit_EU)
                    result2 += alfavit_EU[new_place]
                else:
                    result2 += i
        print(result2)

    elif a == 3:
        print("До свидания!")
        break
    
    else:
        print("Неверный выбор операции. Пожалуйста, выберите 1 для шифровки, 2 для дешифровки или 3 для выхода.")
