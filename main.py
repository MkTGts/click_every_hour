from datetime import datetime
import os
import smtplib


def clicker():  # собирае тотметки через нажатие на энтер и записывает в файл определнного дня
    s = input("Нажмите Enter")
    time_now_to_datetime = datetime.now()  # время сейчас
    time_to_wirte = time_now_to_datetime.strftime("%d.%m.%y  %H:%M:%S")
    file_name = f"data/file_{time_now_to_datetime.strftime('%d_%m_%y')}.txt"
    with open(file_name, 'a', encoding="utf-8") as file:
        file.write(time_to_wirte + '\n')
    os.system("clear")
    print(f"Все Ok. Следующее нажатие ожидается в {time_now_to_datetime.hour}:{time_now_to_datetime.minute}\n")
 

def mail():
    smtpObj = smtplib.SMTP("smtp.rambler.ru", 587)  # подкл к серверку smtp
    smtpObj.starttls()  # шифровагие TLS
    smtpObj.login("mktgts@rambler.ru", "MrSpock14")  # авторизация на smtp server
    smtpObj.sendmail("maksimkor96@yandex.ru", "Hello!")  # адреса почты на которые будем отправлять




def main():
    while True:
        try:
            clicker()
        except Exception as err:
            print(f"При работе возникла ошибка {err}. Попробуйте еще раз или обратитесь к администартору.")


if __name__ == '__main__':
    mail()

