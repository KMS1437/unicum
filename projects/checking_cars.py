import re

def check_number(number):
    private_pattern = r'^[АВЕКМНОРСТУХABEKMHOPCTYXавекмнопрстухabekmhopctyx]\d{3}[АВЕКМНОРСТУХABEKMHOPCTYXавекмнопрстухabekmhopctyx]{2}\d{2,3}$'
    taxi_pattern = r'^[АВЕКМНОРСТУХABEKMHOPCTYXавекмнопрстухabekmhopctyx]{2}\d{5,6}$'

    if re.match(private_pattern, number):
        return "Private"
    elif re.match(taxi_pattern, number):
        return "Taxi"
    else:
        return "Fail"

number = input("введите номер: ")
result = check_number(number)
print(result)

