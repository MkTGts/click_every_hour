from datetime import datetime



while True:
    s = input("Нажмите Enter")
    time_now = datetime.now()
    time_string = time_now.strftime("%d.%m.%y  %H:%M:%S")
    file_name = f'data/file_{time_now.strftime("%d_%m_%y")}.txt'
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(time_string + '\n')
    print(f"Все OK, следующее нажатие должно быть в {f'{time_now.hour + 1}:{time_now.minute}'}")