import speech_recognition as sr 
import webbrowser as wb 
import os 
import sys
import time
from Audio.sound import Sound
from urllib.parse import quote_plus

recog = sr.Recognizer()
print("Здравствуйте! Я вас слушаю") # Приветствие 

def record(): #Запись голоса и перевод в текст
    mic = sr.Microphone()
    with mic:
        recognized_data = ""
        audio = recog.listen(mic, 5, 5) 
        print("Прослушивание завершено!")
        try:
            recognized_data = recog.recognize_google(audio, language="ru").lower() 
            print(recognized_data)
        except sr.UnknownValueError: #Если команда не разобрана
            print("Команда не распознана") 
        return recognized_data

def command(words):  #Создание команды
        for x in words:
            if x in recognized_data:
                return True

def commands(recognized_data): #Функция, отвечающая за выполнение команд
    #З1 - Открытие диспетчера задач:
    if command(["открой диспетчер задач"]):
        print("Открываю...")
        os.system("taskmgr")

    #З2 - Открытие настроек операционной системы:
    if command(["открой панель управления"]):
        print("Сейчас открою") 
        os.system("control")   

    #З3 - Поиск в интернете:
    if command(["поиск в интернете"]):
        call = recognized_data.split(" ",3)[3]  #Удаление первых трёх слов
        wb.open_new_tab("https://yandex.ru/search/?text=" + quote_plus(call) + "&clid=2100784-306&banerid=6302000000%3A5e0887dc35a2d000254ec9d6&win=417&lr=37143")
        print("Смотрите, что я вам смогла найти!")

    #З4 - Закрытие голосового ассистента:
    if command(["пока", "выключись", "увидимся"]):   
        print("Пока!")
        sys.exit()  
     
    #З5 - Открыть файл hosts в блокноте:
    if command(["открой hosts", "открой файл hosts", "открой файл хостс", "открой хостс", "открой hosts в блокноте", "открой файл hosts в блокноте", "открой хостс в блокноте", "открой файл хостс в блокноте"]):
        print("Секунду...")
        os.system("Notepad C:/Windows/System32/drivers/etc/hosts")

    #З6 - Установка громкости на N: 
    if command(["поставь громкость", "установи громкость"]):
        vol = int(recognized_data.split(" ",2)[2]) #Удаление первых двух слов
        Sound.volume_set(vol)

    #З7 - Умножение двух чисел
    if command(["x"]):
        znak = recognized_data.split(" ")[1] 
        if znak == "x": 
            print(int(recognized_data.split()[0]) * int(recognized_data.split()[2])) # Умножение первого и второго числа
        else:
            print("Не правильно назван знак!")
    else:
        print("Команда не найдена!")

# "Бесконечно" работающая программа
while True:
    recognized_data = record()
    commands(recognized_data) 
