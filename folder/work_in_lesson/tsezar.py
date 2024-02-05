alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
offset = int(input('Шаг шифровки: '))
message = input("Сообщение для шифровки: ").upper()
result = ''
lang = input('Выберите язык RU/EU: ')
if lang == 'RU':
    for i in message:
        place = alfavit_RU.find(i)
        new_place = place + offset
        if i in alfavit_RU:
            result += alfavit_RU[new_place]
        else:
            result += i
else:
    for i in message:
        place = alfavit_EU.find(i)
        new_place = place + offset
        if i in alfavit_EU:
            result += alfavit_EU[new_place]
        else:
            result += i
print (result)

alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
offset = int(input('Шаг шифровки: '))
message = input("Сообщение для ДЕшифровки: ").upper()
result2 = ''
if lang == 'RU':
    for i in message:
        place = alfavit_RU.find(i)
        new_place = place - offset
        if i in alfavit_RU:
            result2 += alfavit_RU[new_place]
        else:
            result2 += i
else:
    for i in message:
        place = alfavit_EU.find(i)
        new_place = place - offset
        if i in alfavit_EU:
            result2 += alfavit_EU[new_place]
        else:
            result2 += i
print(result2)
