import random

def load_cities(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        cities = [line.strip() for line in file]
    return cities

def play_cities_game(file_path):
    cities = load_cities(file_path)
    
    print("Добро пожаловать в игру 'Города'!")
    print("Правила: введите название города, начинающееся на последнюю букву предыдущего города.")
    print("Первый город: Москва")
    
    used_cities = set()
    current_city = "Москва"
    
    while True:
        player_city = input(f"Ваш ход ({current_city}): ").capitalize()
        
        if player_city == 'Выход':
            print("Игра завершена.")
            break
        
        if player_city not in cities or player_city in used_cities:
            print("Город недопустим. Попробуйте еще раз.")
            continue
        
        if (player_city[0].lower() != current_city[-1].lower() and
            (player_city[0].lower() not in ['ь', 'ы'] or
             player_city[1:].lower() != current_city[-1].lower()) and
            player_city.split('-')[0].lower() != current_city[-1].lower()):
            print(f"Город должен начинаться на букву '{current_city[-1].upper()}' или '{current_city.split('-')[-1][-1].upper()}'. Попробуйте еще раз.")
            continue
        
        used_cities.add(player_city)
        current_city = player_city
        
        computer_city = find_computer_city(cities, used_cities, current_city)
        if computer_city:
            print(f"Компьютер: {computer_city}")
            used_cities.add(computer_city)
            current_city = computer_city
        else:
            print("Победа! Компьютер не знает больше городов.")
            break

def find_computer_city(all_cities, used_cities, current_city):
    possible_cities = [city for city in all_cities if
                       city[0].lower() == current_city[-1].lower() or
                       (city[0].lower() in ['ь', 'ы'] and city[1:].lower() == current_city[-1].lower()) or
                       (city.startswith('ь') and city.split('-')[-1].lower().startswith(current_city[-1].lower()))
                       and city not in used_cities]
    if possible_cities:
        return random.choice(possible_cities)
    else:
        return None

if __name__ == "__main__":
    file_path = r"C:\Users\kamoz\OneDrive\Рабочий стол\projects\cities\города.txt"
    play_cities_game(file_path)
