a=str(str("Вы хотите ШИФРОВКА/РАСШИФРОВКА: "))
if a == 'ШИФРОВКА':
    alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    smeshenie = int(input('Шаг шифровки: '))
    message = input("Сообщение для шифровки: ").upper()
    itog = ''
    lang = input('Выберите язык RU/EU: ')
    if lang == 'RU':
        for i in message:
            mesto = alfavit_RU.find(i)
            new_mesto = mesto + smeshenie
            if i in alfavit_RU:
                itog += alfavit_RU[new_mesto]
            else:
                itog += i
    else:
        for i in message:
            mesto = alfavit_EU.find(i)
            new_mesto = mesto + smeshenie
            if i in alfavit_EU:
                itog += alfavit_EU[new_mesto]
            else:
                itog += i
    print(itog)
if a == 'РАСШИФРОВКА':
    alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    smeshenie = int(input('Шаг шифровки: '))
    message = input("Сообщение для ДЕшифровки: ").upper()
    itog2 = ''
    if lang == 'RU':
        for i in message:
            mesto = alfavit_RU.find(i)
            new_mesto = mesto - smeshenie
            if i in alfavit_RU:
                itog2 += alfavit_RU[new_mesto]
            else:
                itog2 += i
    else:
        for i in message:
            mesto = alfavit_EU.find(i)
            new_mesto = mesto - smeshenie
            if i in alfavit_EU:
                itog2 += alfavit_EU[new_mesto]
            else:
                itog2 += i
    print(itog2)
